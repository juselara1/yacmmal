import yaml
from typing import Type
from yacmmal.load.base import Loader
from yacmmal.types.base import TDataClass

class YAMLLoader(Loader):
    """
    Loader for YAML files.
    """
