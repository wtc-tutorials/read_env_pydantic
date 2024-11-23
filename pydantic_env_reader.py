from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str
    password: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def main():
    settings = Settings()

    print(settings)


if __name__ == "__main__":
    main()
