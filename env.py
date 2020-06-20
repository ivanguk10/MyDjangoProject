import environ

__all__ = (
    'env',
)

env = environ.Env()

# read .env file from default location or ENV_FILE_PATH
env.read_env(
    env.path(
        'ENV_FILE_PATH',
        default=(environ.Path(__file__) - 1).path('.env')())())