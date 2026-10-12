import logging
import time

import pytest

from helper.decorators import retry, timeit


def test_retry_success():
    calls = {'count': 0}
    times = 3
    @retry(times=times, delay=0, exceptions=(ConnectionError,))
    def func():
        calls['count'] += 1

        if calls['count'] < times:
            raise ConnectionError("temporary error")

        return 'ok'

    result = func()

    assert result == 'ok'
    assert calls['count'] == times


def test_retry_after_error():
    calls = {'count': 0, 'raise': 0}
    times = 3
    @retry(times=times, delay=0, exceptions=(ConnectionError,))
    def func():
        calls['count'] += 1

        if calls['count'] < times:
            calls['raise'] += 1
            raise ConnectionError()

        return 'ok'

    result = func()

    assert result == 'ok'
    assert calls['count'] == times
    assert calls['raise'] == times-1


def test_retry_exception():
    calls = {'count': 0}
    times = 3

    @retry(times=times, delay=0, exceptions=(ConnectionError,))
    def func():
        calls['count'] += 1
        raise ConnectionError("temporary error")

    with pytest.raises(ConnectionError):
        func()

    assert calls['count'] == times


def test_retry_exception_black_list():
    calls = {'count': 0}
    times = 3

    @retry(times=times, delay=0, exceptions=(ConnectionError,))
    def func():
        calls['count'] += 1
        raise ZeroDivisionError("Не то чето")

    with pytest.raises(ZeroDivisionError):
        func()

    assert calls['count'] == 1


def test_timeit():
    @timeit
    def func():
        time.sleep(1)
        return 'ok'

    result = func()
    assert result == 'ok'


def test_timeit_logs(caplog):
    @timeit
    def func():
        time.sleep(1)
        return 'ok'

    with caplog.at_level(logging.WARNING):
        result = func()

    assert 'Finished func' in caplog.text
    assert result == 'ok'

def test_timeit_exception():
    @timeit
    def func():
        time.sleep(1)
        raise ZeroDivisionError("Че-то не то")

    with pytest.raises(ZeroDivisionError):
        func()





