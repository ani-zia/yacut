import secrets

from settings import DEFAULT_LINK_LENGHT_NBYTES


def get_unique_short_id():
    return secrets.token_urlsafe(DEFAULT_LINK_LENGHT_NBYTES)
