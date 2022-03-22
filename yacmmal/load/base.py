import os
from abc import ABC, abstractmethod
from yacmmal.types.config import Config, ConfigAttrs
from pydantic import BaseModel
from typing import Dict, Type, Union

class AbstractLoader(ABC):
    """
    Abstract class for config loaders.
    """
    @abstractmethod
    def add_path(
        self, path: str, name: str, dclass: Type[BaseModel]
        ) -> "AbstractLoader":
        ...

    @abstractmethod
    def load(self, path: str, dclass: Type[BaseModel]) -> BaseModel:
        ...

    @abstractmethod
    def extract(self) -> Config:
        ...

class Loader(AbstractLoader):
    """
    Base class for loading config files.
    """
    def __init__(self, base_path: str):
        self.data: Dict[str, BaseModel] = {}
        self.format: str = ""
        self.base_path: str = base_path

    def add_path(self, path: str, name: Union[str, ConfigAttrs], dclass: Type[BaseModel]) -> "Loader":
        """
        Adds a path to the loader.

        Parameters
        ----------
        path : str
            Path to the config file.
        name : Union[str, ConfigAttrs]
            Name of the config file.
        dclass : Type[BaseModel]
            The dataclass to use.

        Returns
        -------
        Loader
            The current loader.
        """
        if isinstance(name, str):
            name = ConfigAttrs[name]
        file_name = ".".join([path, self.format])
        file_path = os.path.join(self.base_path, file_name)
        self.data[name.name] = self.load(file_path, dclass)
        return self

    def extract(self) -> Config:
        """
        Extracts the config object.

        Returns
        -------
        Config
            The config object.
        """
        return Config(**self.data)
