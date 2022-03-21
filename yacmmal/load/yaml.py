import yaml
from typing import Type
from yacmmal.load.base import Loader
from pydantic import BaseModel

class YAMLLoader(Loader):
    """
    Loader for YAML files.

    Attributes
    ----------
    base_path : str
        The base path to the YAML files.
    """

    def __init__(self, base_path: str = "./"):
        super(YAMLLoader, self).__init__(base_path=base_path)
        self.format = "yaml"

    def load(self, path, dclass: Type[BaseModel]) -> BaseModel:
        """
        Loads a YAML file.

        Parameters
        ----------
        path : str
            The path to the YAML file.
        dclass : Type[BaseModel]
            The dataclass to use.

        Returns
        -------
        BaseModel
            The loaded model.
        """
        with open(path, "r") as f:
            data = yaml.load(f, Loader=yaml.Loader)
        return dclass(**data)
