import configparser
from typing import Type
from yacmmal.load.base import Loader
from pydantic import BaseModel

class CONFLoader(Loader):
    """
    Loader for CONF files.

    Attributes
    ----------
    base_path : str
        The base path of the config files.
    """

    def __init__(self, base_path: str):
        super(CONFLoader, self).__init__(base_path=base_path)
        self.format = "conf"

    def load(self, path: str, dclass: Type[BaseModel]) -> BaseModel:
        """
        Loads a TOML file as a dataclass.

        Parameters
        ----------
        path : str
            The path to the CONF file.
        dclass : Type[BaseModel]
            The dataclass to load the CONF file as.

        Returns
        -------
        BaseModel
            The loaded dataclass.
        """
        config = configparser.ConfigParser()
        config.read(path)

        data = {section: dict(config[section]) for section in config.sections()}
        return dclass.parse_obj(data)

class INILoader(CONFLoader):
    """
    Loader for INI files.

    Attributes
    ----------
    base_path : str
        The base path of the config files.
    """
    def __init__(self, base_path: str):
        super(INILoader, self).__init__(base_path=base_path)
        self.format = "ini"

    def load(self, path: str, dclass: Type[BaseModel]) -> BaseModel:
        """
        Loads a INI file as a dataclass.

        Parameters
        ----------
        path : str
            The path to the INI file.
        dclass : Type[BaseModel]
            The dataclass to load the INI file as.
        """
        return super(INILoader, self).load(path=path, dclass=dclass)
