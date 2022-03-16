from pydantic import BaseModel    
from typing import Optional
from yacmmal.types.base import TDataClass

class Config(BaseModel):
    database: Optional[TDataClass]
    hyperparameters: Optional[TDataClass]
    experiment: Optional[TDataClass]
    training: Optional[TDataClass]
    metrics: Optional[TDataClass]
