from sqlalchemy import Column, Integer, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Базовый класс для всех моделей
Base = declarative_base()


class Sample(Base):
	__tablename__ = 'sample'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(CHAR(length=50), nullable=False)
	extension = Column(CHAR(length=10), nullable=False)
	category_id = Column(Integer, ForeignKey('category.id'), nullable=True)

	category = relationship('Category', back_populates='samples')


class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(CHAR(length=50), nullable=False)

	samples = relationship('Sample', back_populates='category')
