import hashlib
from typing import NoReturn, Union

from django.conf import settings
from itsdangerous import URLSafeTimedSerializer
from itsdangerous.exc import BadTimeSignature, SignatureExpired

serializer = URLSafeTimedSerializer(settings.SECRET_KEY, salt="active-email")
serializer.default_signer.default_digest_method = hashlib.sha256

MAX_AGE = 60 * 60 * 3 # The token is valid for just 3 hours


class ExpiredToken(Exception):
    pass


class BadToken(Exception):
    pass


def generate_token(user_id: int):
    return serializer.dumps(user_id)


def validate_token(token: Union[str , bytes], max_age: int = MAX_AGE):
    try:
        data = serializer.loads(token, max_age=max_age)
    except SignatureExpired:
        raise ExpiredToken("Token has expired. request for another token.")
    except BadTimeSignature:
        raise BadToken("Token is invalid.")
    return data