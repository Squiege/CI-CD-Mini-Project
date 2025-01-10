import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:%40Deblin312145@localhost/m13_mp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

    # 'mysql+mysqlconnector://root:%40Deblin312145@localhost/m13_mp' , Old URI