import datetime
import logging
import time
from functools import wraps
from typing import Type, Callable

logger = logging.getLogger(__name__)

def retry(times: int, delay: float, exceptions: tuple[Type[Exception]]):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for i in range(times):
                try:
                    logger.warning(f"start")
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_error = exc
                    logger.warning(f"[{datetime.datetime.now()}] Failed {func.__name__} with {last_error}. Retrying, {i+1}/{times}")
                    if i < times - 1:
                        time.sleep(delay)

            raise last_error
        return wrapper
    return decorator


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end = time.perf_counter()
            log_str = f"[{datetime.datetime.now()}] Finished {func.__name__} with {end-start}"
            logger.warning(log_str)
    return wrapper
