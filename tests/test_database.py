from sqlalchemy import inspect

from yacut.models import URL_map


def test_fields(_app):
    inspector = inspect(URL_map)
    fields = [column.name for column in inspector.columns]
    assert all(field in fields for field in ['id', 'original', 'short', 'timestamp']), (
        'В модели не найдены все необходимые поля. '
        'Проверьте модель: в ней должны быть поля id, original, short и timestamp.'
    )
