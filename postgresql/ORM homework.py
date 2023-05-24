import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

import json

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = ''
engine = sq.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open(r'C:\Users\user\Desktop\tests_data.json', 'r') as f:
    data = json.load(f)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
        }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

def find_sales():
    value = input('Enter publisher id or name for which you would like to display info: ')
    subq = session.query(Publisher).filter(or_(Publisher.id == int(value) if value.isdigit() else None, Publisher.name == value)).subquery()
    query = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).\
        join(subq, subq.c.id == Book.id_publisher).\
        join(Stock, Stock.id_book == Book.id).\
        join(Sale, Sale.id_stock == Stock.id).\
        join(Shop, Shop.id == Stock.id_shop)
    for book_title, shop_name, sale_price, sale_date in query:
        print(book_title, '|', shop_name, '|', sale_price, '|', sale_date)


find_sales()