from model import Pessoa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib

def retornaSession():
    CONNECTION = "sqlite:///sistema_login.db"
    engine = create_engine(CONNECTION, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

class ControllerCadastro:
    @classmethod
    def verificaDados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retornaSession()
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all() # VERIFICA SE O EMAIL JÁ ESTÁ CADASTRADO NO SISTEMA
        if len(usuario) > 0:
            return 5
        dados_verificados = cls.verificaDados(nome, email, senha) # FAZ AS VALIDAÇÕES DOS DADOS
        if dados_verificados != 1: # SE NÃO RETORNAR 1, QUE SERIA TUDO OK
            return dados_verificados # RETORNA O VALOR DO PROBLEMA
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest() # CRIPTOGRAFIA DA SENHA COM sha256
            salva_bd = Pessoa(nome=nome, email=email, senha=senha)
            session.add(salva_bd)
            session.commit()
            return 1
        except:
            return 6 # ERRO INTERNO DO SISTEMA

class ControllerLogin():
    @classmethod
    def login(cls, email, senha):
        session = retornaSession()
        senha = hashlib.sha256(senha.encode()).hexdigest() # CRIPTOGRAFA A SENHA RECEBIDA PARA COMPARAR COM A SENHA NO BD
        verifica_login = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all() # FILTRA OS DADOS DO BD PARA COMPARAR COM OS RECEBIDOS
        if len(verifica_login) == 1: # SE OS DADOS BATEREM COM ALGUM DO BD, RETORNA 1
            return {'logado': True, 'id': verifica_login[0].id} # RETORNA LOGADO TRUE E O ID DO USUARIO
        else:
            return False
