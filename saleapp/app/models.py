from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0.0)
    image = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    activate = Column(Boolean, default=True)

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Laptop')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        pass

