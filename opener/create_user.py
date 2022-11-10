from pydantic.env_settings import BaseSettings
from sqlalchemy.orm.session import Session

from opener.internal.auth import get_password_hash
from opener.internal.database import Base, User, engine


class UserSettings(BaseSettings):
    username: str
    password: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def main() -> None:
    """Create db tables and insert user"""
    print("Creating user")

    Base.metadata.create_all(bind=engine)
    password_hash = get_password_hash(UserSettings().password)
    with Session(engine) as db:
        db.add(User(username=UserSettings().username, hashed_password=password_hash))
        db.commit()


if __name__ == "__main__":
    main()
