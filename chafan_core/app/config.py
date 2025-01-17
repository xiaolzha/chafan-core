import os
from typing import Any, Dict, List, Literal, Optional, Union

import boto3
import sentry_dramatiq
import sentry_sdk
from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, validator
from pydantic.types import SecretStr
from sentry_sdk.integrations.redis import RedisIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

from chafan_core.utils.validators import CaseInsensitiveEmailStr

load_dotenv()


class Settings(BaseSettings):
    ############ Common ############
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    ENV: Literal["dev", "stag", "prod"]
    DB_SESSION_POOL_SIZE: int = 60
    READ_DB_SESSION_POOL_SIZE: int = 60
    DB_SESSION_POOL_MAX_OVERFLOW_SIZE: int = 20
    READ_DB_SESSION_POOL_MAX_OVERFLOW_SIZE: int = 20
    DEFAULT_LOCALE: Literal["en", "zh"] = "zh"
    PROJECT_NAME: str
    SENTRY_DSN: Optional[AnyHttpUrl] = None

    DATABASE_URL: str
    DATABASE_READ_REPLICA_URL: Optional[str] = None
    REDIS_URL: str

    ENABLE_CAPTCHA: bool = False

    EMAILS_FROM_EMAIL: Optional[CaseInsensitiveEmailStr] = None

    INVITE_NEW_USER_COIN_PAYMENT_AMOUNT: int = 5
    CREATE_ARTICLE_COIN_DEDUCTION: int = 2
    UPVOTE_ARTICLE_COIN_DEDUCTION: int = 2
    CREATE_SITE_COIN_DEDUCTION: int = 10
    CREATE_SITE_FORCE_NEED_APPROVAL: bool = True

    ES_ENDPOINT: Optional[AnyHttpUrl] = None
    ES_HTTP_USERNAME: Optional[str] = None
    ES_HTTP_PASSWORD: Optional[str] = None

    EMAILS_FROM_NAME: Optional[str] = None

    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_TEMPLATES_DIR: str = "chafan_core/app/email-templates/build"
    EMAILS_ENABLED: bool = False

    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_REGION: Optional[str] = None
    AWS_CLOUDFRONT_HOST: Optional[AnyHttpUrl] = None
    CLOUDFRONT_HOST: Optional[AnyHttpUrl] = None
    S3_UPLOADS_BUCKET_NAME: Optional[str] = None

    MIN_KARMA_CREATE_PUBLIC_SITE: int = 100
    MIN_KARMA_CREATE_PRIVATE_SITE: int = 10

    MQ_URL: Optional[str] = None
    CLOUDAMQP_URL: Optional[str] = None

    ############ Web server only ############
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: Optional[str] = None
    # 60 minutes * 24 hours * 60 days = 60 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 60
    API_SERVER_SCHEME: str = "https"

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost"]'
    BACKEND_CORS_ORIGINS: List[str] = []

    HCAPTCHA_SITEKEY: str = "10000000-ffff-ffff-ffff-000000000001"
    HCAPTCHA_SECRET: str = "0x0000000000000000000000000000000000000000"

    WELCOME_TEST_FORM_UUID: str = "4CGv4iReMxuWjs3T2PEY"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_SIGNUP_CODE_EXPIRE_HOURS: int = 48
    PHONE_NUMBER_VERIFICATION_CODE_EXPIRE_HOURS: int = 1

    FIRST_SUPERUSER: Optional[CaseInsensitiveEmailStr] = None
    FIRST_SUPERUSER_PASSWORD: Optional[SecretStr] = None
    USERS_OPEN_REGISTRATION: bool = True

    MONGO_CONNECTION: Optional[str] = None

    ES_APM_SECRET_TOKEN: Optional[str] = None
    ES_APM_SERVER_URL: Optional[str] = None

    OFFICIAL_BOT_SECRET: Optional[str] = None

    INFLUXDB_URL: Optional[str] = None
    INFLUXDB_TOKEN: Optional[str] = None
    INFLUXDB_ORG: Optional[str] = None
    INFLUXDB_BUCKET: Optional[str] = None

    FORCE_RATE_LIMIT: bool = False

    class Config:
        case_sensitive = True


setting_keys = set(Settings.schema()["properties"].keys())

_AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
_AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
_AWS_REGION = os.environ.get("AWS_REGION")
_ENV = os.environ.get("ENV")

if _AWS_ACCESS_KEY_ID and _AWS_SECRET_ACCESS_KEY and _AWS_REGION and _ENV == "prod":
    # Override some env vars from parameter store
    ssm = boto3.Session(
        aws_access_key_id=_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=_AWS_SECRET_ACCESS_KEY,
        region_name=_AWS_REGION,
    ).client("ssm")
    for setting_key in setting_keys:
        if setting_key.lower().startswith("aws"):
            continue
        try:
            os.environ[setting_key] = ssm.get_parameter(Name=setting_key)["Parameter"][
                "Value"
            ]
            print(f"Overridden with SSM: {setting_key}")
        except Exception as e:
            if "ParameterNotFound" in str(e):
                continue
            print(setting_key, type(e))


settings = Settings()

# TODO: migrate
if settings.AWS_CLOUDFRONT_HOST is None:
    settings.AWS_CLOUDFRONT_HOST = settings.CLOUDFRONT_HOST


def get_mq_url() -> str:
    url = settings.MQ_URL or settings.CLOUDAMQP_URL
    assert url is not None
    return url


if settings.SENTRY_DSN:
    sentry_sdk.init(
        settings.SENTRY_DSN,
        traces_sample_rate=0.2,
        integrations=[
            RedisIntegration(),
            SqlalchemyIntegration(),
            sentry_dramatiq.DramatiqIntegration(),
        ],
    )
