import toml
from typing import Type
from yacmmal.load.base import Loader
from pydantic import BaseModel

class TOMLLoader(Loader):
    """
    Loader for TOML files.

    Attributes
    ----------
    base_path : str
        The base path of the config files.
    """

    def __init__(self, base_path: str):
        super(TOMLLoader, self).__init__(base_path=base_path)
        self.format = "toml"

    def load(self, path: str, dclass: Type[BaseModel]) -> BaseModel:
        """
        Loads a TOML file as a dataclass.

        Parameters
        ----------
        path : str
            The path to the TOML file.
        dclass : Type[BaseModel]
            The dataclass to load the TOML file as.

        Returns
        -------
        BaseModel
            The loaded dataclass.
        """
        with open(path, "r") as json_file:
            data = toml.load(json_file)
        return dclass.parse_obj(data)
