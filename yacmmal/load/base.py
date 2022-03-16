import os
from abc import ABC, abstractmethod
from yacmmal.types.config import Config
from pydantic import BaseModel
from typing import Dict, Type

class AbstactLoader(ABC):

    @abstractmethod
    def add_path(self, path: str, name: str, dclass: Type[BaseModel]) -> "AbstactLoader":
        ...

    @abstractmethod
    def load(self, path: str, dclass: Type[BaseModel]) -> BaseModel:
        ...

    @abstractmethod
    def extract(self) -> Config:
        ...

class Loader(AbstactLoader):
    def __init__(self, base_path: str):
        self.data: Dict[str, BaseModel] = {}
        self.format: str = ""
        self.base_path: str = base_path

    def add_path(self, path: str, name: str, dclass: Type[BaseModel]) -> "Loader":
        file_name = ".".join([path, self.format])
        file_path = os.path.join(self.base_path, file_name)
        self.data[name] = self.load(file_path, dclass)
        return self

    def extract(self) -> Config:
        return Config(**self.data)
