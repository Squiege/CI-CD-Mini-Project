import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://ci_cd_mini_project_user:oVppz93WJsVYc17u9ziXjknmH5E6gYok@dpg-ctv6uitds78s738ouko0-a:5432/ci_cd_mini_project'
    )
    DEBUG = True

    # 'mysql+mysqlconnector://root:%40Deblin312145@localhost/m13_mp' , Old URI