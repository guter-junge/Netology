import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'Publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'Publisher {self.id}: {self.name}'


class Book(Base):
    __tablename__ = 'Book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=100), unique=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('Publisher.id'), nullable=False)

    publisher = relationship(Publisher, backref='books')

    def __str__(self):
        return f'Book {self.id}: {self.title}, {self.id_publisher}'

class Shop(Base):
    __tablename__ = 'Shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=100), unique=False)

    def __str__(self):
        return f'Shop {self.id}: {self.name}'


class Stock(Base):
    __tablename__ = 'Stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('Book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('Shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    shop = relationship(Shop, backref='shop_stocks')
    book = relationship(Book, backref='book_stocks')

    def __str__(self):
        return f'Stock {self.id}: {self.count}, {self.id_book}, {self.id_shop}'


class Sale(Base):
    __tablename__ = 'Sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('Stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref='sales')

    def __str__(self):
        return f'Sale {self.id}: {self.price}, {self.date_sale}, {self.id_stock}, {self.count}'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


