from sqlalchemy import Column, Integer, Float, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Criando uma engine (arquivo local)
engine = create_engine('sqlite:///menu.db', echo=True)

Base = declarative_base()

# Criando os cadastros


class Produto(Base):
    __tablename__ = "Produto"
    codigo = Column(Integer, primary_key=True)
    descricao = Column(String(250))
    preco = Column(Float)

    def __repr__(self):
        return f'<Produto {self.codigo}'


class Cliente(Base):
    __tablename__ = "Cliente"
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(250))

    def __repr__(self):
        return f'<Cliente {self.nome}'


class Vendedor(Base):
    __tablename__ = "Vendedor"
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(250))

    def __repr__(self):
        return f'<Vendedor {self.nome}'


# Criando o banco de dados
Base.metadata.create_all(engine)
