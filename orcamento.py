from sqlalchemy import Column, Integer, Float, ForeignKey, Time, CheckConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship

# Criando uma engine (arquivo local)
engine = create_engine('sqlite:///orcamento.db', echo=True)

Base = declarative_base()

# Criando o orçamento


class Orcamento(Base):
    __tablename__ = "Orcamento"
    __table_args__ = (
        CheckConstraint("vendedor_id != cliente_id")
    )
    codigo = Column(Integer, primary_key=True)
    vendedor_id = Column(Integer, ForeignKey("Vendedor.codigo"))
    cliente_id = Column(Integer, ForeignKey("Cliente.codigo"))
    data = Column(Time)
    total = Column(Float)

    vendedor_id = relationship("Vendedor")
    cliente_id = relationship("Cliente")

    def __repr__(self):
        return f'<Orcamento {self.codigo}'


class ItemOrcamento(Base):
    __tablename__ = "Item_orçamento"
    codigo = Column(Integer, primary_key=True)
    orcamento_id = Column(Integer, ForeignKey("Orcamento.codigo"))
    produto_id = Column(Integer, ForeignKey("Produto.codigo"))
    quantidade = Column(Integer)
    preco_unitario = Column(Float)
