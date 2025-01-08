from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Customer(Base):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(db.String(320), nullable=False)

    # Relationships
    orders: Mapped[list['Order']] = relationship('Order', back_populates='customer')
    customer_account: Mapped['CustomerAccount'] = relationship('CustomerAccount', back_populates='customer')
