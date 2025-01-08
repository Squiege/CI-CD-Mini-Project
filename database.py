from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

class Base(declarative_base):
    pass

db = SQLAlchemy()
Base = declarative_base()