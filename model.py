from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONNECTION = "sqlite:///sistema_login.db"

engine = create_engine(CONNECTION, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(200))
    senha = Column(String(100)) # DEVE-SE COLOCAR O TAMANHO QUE A CRIPTOGRAFIA SUPORTE

Base.metadata.create_all(engine)
