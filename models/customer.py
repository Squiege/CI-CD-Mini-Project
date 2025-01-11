from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, db

class Customer(Base):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(db.String(320), nullable=False)

    # Relationships
    orders: Mapped[list['Order']] = db.relationship('Order', back_populates='customer')
    customer_account: Mapped['CustomerAccount'] = db.relationship('CustomerAccount', back_populates='customer')
