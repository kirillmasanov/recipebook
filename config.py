class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kirill:123@localhost/recipebook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
