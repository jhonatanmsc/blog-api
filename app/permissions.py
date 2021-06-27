import pdb

from fastapi import HTTPException

from app.settings import SECRET_PASS


def is_authenticated(*types):
    def decorator(f):
        def new_f(*args, **kwargs):
            if args[0] == SECRET_PASS:
                return f(args, kwargs)
            else:
                raise HTTPException(status_code=401, detail="Not permission.")
        return new_f
    return decorator
