from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_password: str = "your_datebase_pass"
    database_name: str = "your_datebase_name"
    database_username: str = "your_datebase_username"
    access_token_expire_minute: int = 15

    class Config:
        env_file = ".env"

settings = Settings()


