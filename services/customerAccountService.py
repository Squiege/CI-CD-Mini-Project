from sqlalchemy import select
from models.customerAccount import CustomerAccount
from database import db

def find_all_accounts():
    query = select(CustomerAccount)
    return db.execute(query).scalars().all()

def find_account_by_id(account_id):
    query = select(CustomerAccount).filter(CustomerAccount.id == account_id)
    return db.execute(query).scalar()

def create_account(account):
    db.add(account)
    db.commit()

def update_account(account_id, account):
    query = select(CustomerAccount).filter(CustomerAccount.id == account_id)
    existing_account = db.execute(query).scalar()
    existing_account.balance = account.balance
    db.commit()

def delete_account(account_id):
    query = select(CustomerAccount).filter(CustomerAccount.id == account_id)
    existing_account = db.execute(query).scalar()
    db.delete(existing_account)
    db.commit()