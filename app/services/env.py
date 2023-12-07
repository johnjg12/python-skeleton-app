import os


def get_hostname() -> str:
    return get_envar_or_fail('HOSTNAME')


def get_app_url() -> str:
    ret = get_envar('APP_URL')
    if ret is None:
        ret = f'http://{get_hostname()}:{get_app_port()}'
    return ret


def get_app_port() -> int:
    ret = get_envar('APP_PORT')
    if ret is None:
        ret = '8000'
    return int(ret)


def get_envar(envar: str) -> str | None:
    return os.getenv(envar)


def get_envar_or_fail(envar: str) -> str:
    ret = get_envar(envar)
    if ret is None:
        raise ValueError(f"Unable to find environment variable '{envar}'!")
    return ret
