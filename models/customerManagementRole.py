from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db, Base

class CustomerManagementRole(Base):
    __tablename__ = 'customer_management_roles'

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_account_id: Mapped[int] = mapped_column(db.ForeignKey('customer_accounts.id'))
    role_id: Mapped[int] = mapped_column(db.ForeignKey('roles.id'))

    # Relationships
    customer_account: Mapped['CustomerAccount'] = relationship('CustomerAccount', back_populates='roles')
    role: Mapped['Role'] = relationship('Role', back_populates='customer_management_roles')
