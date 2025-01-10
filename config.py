import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://ci_cd_mini_project_user:oVppz93WJsVYc17u9ziXjknmH5E6gYok@dpg-ctv6uitds78s738ouko0-a/ci_cd_mini_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

    # 'mysql+mysqlconnector://root:%40Deblin312145@localhost/m13_mp' , Old URI