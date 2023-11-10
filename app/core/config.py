from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = 'postgresql://postgres:SeeD0409!@localhost:5432/SeaSaba'
    secret_key: str = 'insert_a_very_secret_key_here'
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 60
    
settings = Settings()