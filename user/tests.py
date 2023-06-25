from django.test import TestCase

from werkzeug.security import generate_password_hash, check_password_hash

hash = generate_password_hash('xiaoshen')
h = check_password_hash(hash, 'xiaoshen')
print(h)

import hashlib


def make_password(password):
    # md5
    md5 = hashlib.md5()
    # 转码
    sign_utf8 = str(password).encode(encoding="utf-8")
    # 加密
    md5.update(sign_utf8)
    # 返回密文
    return md5.hexdigest()

