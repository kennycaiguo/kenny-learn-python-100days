import hashlib

from day47 import settings

def md5(pwd):
    mobj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    mobj.update(pwd.encode('utf-8'))
    return mobj.hexdigest()