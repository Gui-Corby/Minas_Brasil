from sqlalchemy import Column, ForeignKey, Integer, CheckConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship

# Criando uma engine (arquivo local)
engine = create_engine('sqlite:///oferta.db', echo=True)

Base = declarative_base()

# Criando a oferta


class Oferta(Base):
    __tablename__ = "Oferta"
    __table_args__ = (
        CheckConstraint("quant_pagar > quant_levar"), )
    codigo = Column(Integer, primary_key=True)
    id_produto = Column(
                Integer,
                ForeignKey("Produto.codigo")
                 )
    quant_levar = Column(Integer)
    quant_pagar = Column(Integer)

    id_produto = relationship("Produto")

    def __repr__(self):
        return f'<Oferta {self.codigo}'


# Criando o banco de dados
Base.metadata.create_all(engine)
