import re
from http import HTTPStatus

from flask import jsonify, request

from settings import REGEX_PATTERN, USER_LINK_LENGHT

from . import app, db
from .error_handlers import APIUsageError
from .models import URL_map
from .utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_link():
    data = request.get_json()
    if not data:
        raise APIUsageError('Отсутствует тело запроса')
    original = data.get('url')
    if not original:
        raise APIUsageError('"url" является обязательным полем!')
    custom_short = data.get('custom_id')
    if custom_short:
        if len(custom_short) > USER_LINK_LENGHT or not re.match(REGEX_PATTERN,
                                                                custom_short):
            raise APIUsageError('Указано недопустимое имя для короткой ссылки')
        if URL_map.query.filter_by(short=custom_short).first():
            raise APIUsageError(f'Имя "{custom_short}" уже занято.')
    else:
        custom_short = get_unique_short_id()
    sortened_link = URL_map(
        original=original,
        short=custom_short
    )
    db.session.add(sortened_link)
    db.session.commit()
    return jsonify(sortened_link.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_url(short):
    original_url = URL_map.query.filter_by(short=short).first()
    if not original_url:
        raise APIUsageError('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': original_url.original}), HTTPStatus.OK
