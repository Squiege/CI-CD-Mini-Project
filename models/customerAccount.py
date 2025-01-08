from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class CustomerAccount(Base):
    __tablename__ = 'customer_accounts'

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'), nullable=False)
    username: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(80), nullable=False)

    # Relationships
    customer: Mapped['Customer'] = relationship('Customer', back_populates='customer_account')
    roles: Mapped[list['CustomerManagementRole']] = relationship('CustomerManagementRole', back_populates='customer_account')