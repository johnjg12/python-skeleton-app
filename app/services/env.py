import os


def get_hostname() -> str:
    return get_envar('HOSTNAME')


def get_envar(envar: str) -> str:
    ret = os.getenv(envar)
    if ret is None:
        raise ValueError(f"Unable to find environment variable '{envar}'!")
    return ret
