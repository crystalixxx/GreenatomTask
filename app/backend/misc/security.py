import datetime
import jwt

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from app.backend.misc.config import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authentication/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(*, data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.now(tz=datetime.timezone.utc) + expires_delta
    else:
        expire = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(
            minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, config.SECURITY_KEY, algorithm=config.SECURITY_ALGORITHM
    )

    return encoded_jwt