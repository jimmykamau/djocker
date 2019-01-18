import os


current_environment = os.getenv("ENVIRONMENT_SETTINGS")

if current_environment == "PRODUCTION":
    from djocker.settings.production import *
elif current_environment == "DEVELOPMENT":
    from djocker.settings.development import *
