from pydantic import BaseModel    
from typing import Optional
from enum import Enum, auto

class Config(BaseModel):
    """
    The default configuration dataclass of yacmmal.
    """
    paths: Optional[BaseModel]
    database: Optional[BaseModel]
    hyperparameters: Optional[BaseModel]
    experiment: Optional[BaseModel]
    training: Optional[BaseModel]
    evaluation: Optional[BaseModel]
    optimization: Optional[BaseModel]
    deploy: Optional[BaseModel]

class ConfigAttrs(Enum):
    """
    The attributes supported by yacmmal's Config dataclass.
    """
    paths = auto()
    database = auto()
    hyperparameters = auto()
    experiment = auto()
    training = auto()
    evaluation = auto()
    optimization = auto()
    deploy = auto()
