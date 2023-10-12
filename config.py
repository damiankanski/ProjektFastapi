from pydantic_settings import BaseSettings
from pydantic import Field



class Settings(BaseSettings):
    database_hostname: str = Field(env="DB_HOST")
    database_port: int = Field(env="DB_PORT")
    database_password: str = Field(env="DB_PASSWORD")
    database_name: str = Field(env="DB_NAME")
    database_username: str = Field(env="DB_USERNAME")
    access_token_expire_minute: int = Field(env="ACCESS_TOKEN")

    class Config:
        env_file = ".env"


settings = Settings()
