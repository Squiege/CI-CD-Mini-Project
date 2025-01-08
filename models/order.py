from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.ForeignKey('products.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    total_price: Mapped[float] = mapped_column(nullable=False)

    # Relationships
    customer: Mapped['Customer'] = relationship('Customer', back_populates='orders')
    product: Mapped['Product'] = relationship('Product', back_populates='orders')
