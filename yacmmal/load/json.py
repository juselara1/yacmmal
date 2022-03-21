import json
from typing import Type
from yacmmal.load.base import Loader
from pydantic import BaseModel

class JSONLoader(Loader):
    """
    Loader for JSON files.

    Attributes
    ----------
    base_path : str
        The base path of the config files.
    """

    def __init__(self, base_path: str):
        super(JSONLoader, self).__init__(base_path=base_path)
        self.format = "json"

    def load(self, path, dclass: Type[BaseModel]) -> BaseModel:
        """
        Loads a JSON file as a dataclass.

        Parameters
        ----------
        path : str
            The path to the JSON file.
        dclass : Type[BaseModel]
            The dataclass to load the JSON file as.

        Returns
        -------
        BaseModel
            The loaded dataclass.
        """
        with open(path, "r") as json_file:
            data = json.load(json_file)
        return dclass(**data)
