from .__init__ import app, db
from flask_sqlalchemy import SQLAlchemy
from .setup import properties, query

class Property(db.Model):
    __tablename__ = "properties"
    property_id = db.Column('prop_id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(40))
    no_bed = db.Column('no_bed', db.Integer)
    no_bath = db.Column('no_bath', db.Integer)
    location = db.Column('location', db.String(40))
    desc = db.Column('descr', db.String(255))
    typ = db.Column('typ', db.String(15))
    price = db.Column('price', db.Float)
    media_addr = db.Column('media_addr', db.String(60))

    def __init__(self, title, no_bed, no_bath, location, desc, typ, price, media_addr):
        try:
            self.title = title
            self.no_bed = no_bed
            self.no_bath = no_bath
            self.location = location
            self.desc = desc
            self.typ = typ
            self.price = price
            self.media_addr = media_addr

            ins = properties.insert().values(title = self.title, no_bed = self.no_bed, no_bath = self.no_bath, loc = self.location, \
                                                descr = self.desc, typ = self.typ, price = self.price, media_addr = self.media_addr)
            print(ins)
            result = query(ins)
            print(result)
        except Exception as e:
            print("Error occurred:\n{}\n".format(e))
