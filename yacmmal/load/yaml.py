import yaml
from typing import Type
from yacmmal.load.base import Loader
from pydantic import BaseModel

class YAMLLoader(Loader):
    """
    Loader for YAML files.
    """

    def __init__(self, base_path: str = "./"):
        super(YAMLLoader, self).__init__(base_path=base_path)
        self.format = "yaml"

    def load(self, path, dclass: Type[BaseModel]) -> BaseModel:
        with open(path, "r") as f:
            data = yaml.load(f, Loader=yaml.Loader)
        return dclass(**data)
