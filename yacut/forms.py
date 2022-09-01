from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from settings import DEFAULT_LINK_LENGHT, USER_LINK_LENGHT, REGEX_PATTERN


class LinkForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'), URL(message='Введите ссылку целиком')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(min=DEFAULT_LINK_LENGHT, max=USER_LINK_LENGHT,
                           message=f'Длина ссылки должна быть от {DEFAULT_LINK_LENGHT} до {USER_LINK_LENGHT} символов'),
                    Regexp(REGEX_PATTERN,
                           message='Можно использовать только латинские буквы и арабские цифры'),
                    Optional()]
    )
    submit = SubmitField('Создать')
