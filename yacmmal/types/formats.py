from enum import Enum, auto

class ConfigFormat(Enum):
    """
    Enum for the different formats of the data.
    """
    JSON = auto()
    YAML = auto()
    TOML = auto()
    CONF = auto()
