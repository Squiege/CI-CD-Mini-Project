from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, db

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.ForeignKey('products.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False)
    total_price: Mapped[float] = mapped_column(db.Float, nullable=False)

    # Relationships
    customer: Mapped['CustomerAccount'] = db.relationship('Customer', back_populates='orders')
    product: Mapped['Role'] = db.relationship('Product', back_populates='orders')

