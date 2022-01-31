from os import environ


def _create_sql_alchemy_url(
    db_url: str, db_user: str, db_pass: str, db_name: str
) -> str:
    return "postgresql+psycopg2://%(user)s:%(pass)s@%(url)s/%(name)s" % {
        "user": db_user,
        "pass": db_pass,
        "name": db_name,
        "url": db_url,
    }


class Config:
    """
    Common configurations
    """

    LOG_LEVEL = environ.get("advertisement_analysis_LOG_LEVEL", "DEBUG")
    LOG_FORMAT = environ.get("advertisement_analysis_LOG_FORMAT", "console").lower()
    SQLALCHEMY_ECHO = environ.get("SQLALCHEMY_ECHO", "false") == "true"

    STATSD_API_KEY = environ.get("advertisement_analysis_STATSD_API_KEY")
    STATSD_APP_KEY = environ.get("advertisement_analysis_STATSD_APP_KEY")

    """
    - ADERTISEMENT_DB_URL=advertisement_analysis_db
      - ADERTISEMENT_DB_USER=adjust_user
      - ADERTISEMENT_DB_PASS=adjust_user
      - ADERTISEMENT_DB_NAME=advertisement_analysis
    """

    db_url = environ.get("ADERTISEMENT_DB_URL", "advertisement_analysis_db")
    db_user = environ.get("ADERTISEMENT_DB_USER", "adjust_user")

    db_pass = environ.get("ADERTISEMENT_DB_PASS", "adjust_user")
    db_name = environ.get("ADERTISEMENT_DB_NAME", "adjust_user")

    SQLALCHEMY_DATABASE_URI = _create_sql_alchemy_url(db_url, db_user, db_pass, db_name)

    ADJUST_DATA_URL = environ.get(
        "ADJUST_DATA_URL", "https://gist.githubusercontent.com"
    )
