import secrets

from settings import DEFAULT_LINK_LENGHT_NBYTES

from .models import URL_map


def get_unique_short_id():
    short_link = secrets.token_urlsafe(DEFAULT_LINK_LENGHT_NBYTES)
    if URL_map.query.filter_by(short=short_link).first():
        return get_unique_short_id()
    return short_link
