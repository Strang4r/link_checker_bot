from typing import Callable, List

from dependency_injector.containers import Container
from app.internal.telegram import Telegram


def __wire_packages(
    container: Callable[..., Container],
    pkg_name: str,
    packages: List[str],
):
    container().wire(packages=[pkg_name, *packages])


def register_container(pkg_name: str, packages: List[str] = None) -> None:
    """Function for wire all containers.

    :param packages: packages to which the injector will be available.
    :param pkg_name: __name__ of main package.
    Returns: None
    """
    if packages is None:
        packages = ["app.internal"]

    __wire_packages(Telegram, pkg_name=pkg_name, packages=packages)
