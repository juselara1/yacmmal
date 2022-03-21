import json
from typing import Type
from yacmmal.load.base import Loader
from pydantic import BaseModel


class JSONLoader(Loader):
    """
    Loader for JSON files.
    """

    def __init__(self, base_path: str):
        super(JSONLoader, self).__init__(base_path=base_path)
        self.format = "json"

    def load(self, path, dclass: Type[BaseModel]) -> BaseModel:
        with open(path, "r") as json_file:
            data = json.load(json_file)
        return dclass(**data)
