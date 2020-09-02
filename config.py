class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kirill:123@localhost/recipebook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'esfun3rnujnnWnwPV9efemu8127yhfn'
    JWT_ERROR_MESSAGE_KEY = 'message'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    UPLOADED_IMAGES_DEST = 'static/images'
