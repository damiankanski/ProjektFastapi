from pydantic_settings import BaseSettings




class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: int = 5432
    database_password: str = "pass"
    database_name: str = "user"
    database_username: str = "user"
    access_token_expire_minute: int = 15


settings = Settings()
