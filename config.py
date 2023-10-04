from pydantic import BaseSettings

class Settings(BaseSettings):
    database_password: str
    database_name: str
    database_username: str
    access_token_expire_minute: int

    class Config:
        env_file = ".env"

settings = Settings()


