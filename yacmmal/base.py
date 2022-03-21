from pydantic import BaseModel
from yacmmal.load.yaml import YAMLLoader
from yacmmal.load.json import JSONLoader
from typing import Sequence, Tuple, Callable, Type

loaders = {"yaml": YAMLLoader, "json": JSONLoader}


def autoconfig(
    base_path: str, config: Sequence[Tuple[str, str, Type[BaseModel]]], format: str
) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def func_with_conf(*args, **kwargs):
            loader = loaders[format](base_path)
            for path, name, dclass in config:
                loader.add_path(path, name, dclass)
            return func(loader.extract(), *args, **kwargs)

        return func_with_conf

    return wrapper
