from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declared_attr
from fastapi_utils.camelcase import camel2snake

from app.orm.base.main import Base


class lAddressesChainsLabels(Base):

    @declared_attr
    def __tablename__(cls) -> str:
        return camel2snake(cls.__name__)

    l_address_chain_label_id = Column(Integer, primary_key=True)

    l_address_chain_id = Column(Integer, ForeignKey('l_addresses_chains.l_address_chain_id'), nullable=False)
    h_label_id = Column(Integer, ForeignKey('h_labels.h_label_id'), nullable=False)