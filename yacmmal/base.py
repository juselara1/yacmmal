from pydantic import BaseModel
from yacmmal.load.yaml import YAMLLoader
from yacmmal.load.json import JSONLoader
from yacmmal.types.formats import ConfigFormat
from typing import Sequence, Tuple, Callable, Type, Union

loaders = {
        ConfigFormat.YAML: YAMLLoader,
        ConfigFormat.JSON: JSONLoader
        }

def autoconfig(
    base_path: str,
    config: Sequence[Tuple[str, str, Type[BaseModel]]],
    format: Union[str, ConfigFormat],
    ) -> Callable:
    """
    Decorator to automatically load a config file.

    Parameters
    ----------
    base_path : str
        The base path to the config file.
    config : Sequence[Tuple[str, str, Type[BaseModel]]]
        A list of tuples containing the name of the config file, the path to the config file, and the dataclass.
    format : str
        The format of the config file.
    """
    if isinstance(format, str):
        format = ConfigFormat[format.upper()]

    def wrapper(func: Callable) -> Callable:
        def func_with_conf(*args, **kwargs):
            loader = loaders[format](base_path)
            for path, name, dclass in config:
                loader.add_path(path, name, dclass)
            return func(loader.extract(), *args, **kwargs)

        return func_with_conf

    return wrapper
