from flask_caching import Cache
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES

cache = Cache()
db = SQLAlchemy()
image_set = UploadSet('images', IMAGES)
jwt = JWTManager()
limiter = Limiter(key_func=get_remote_address)
