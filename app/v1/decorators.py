from functools import wraps
from typing import Any

from fastapi import HTTPException
from pydantic import ValidationError
from requests.exceptions import JSONDecodeError
from starlette import status


def manage_transaction(func) -> Any:
    """
    Handle session transaction and
    exceptions raised across the running code.
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            rv = await func(*args, **kwargs)
            return rv
        except ValidationError as exc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
        except (
            KeyError,
            TypeError,
            AttributeError,
            JSONDecodeError,
            ValueError,
            TimeoutError,
        ) as exc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.args)
        except HTTPException as exc:
            raise exc
        except Exception as exc:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=exc.args)

    return wrapper
