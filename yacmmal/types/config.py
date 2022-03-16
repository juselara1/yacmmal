from pydantic import BaseModel    
from typing import Optional

class Config(BaseModel):
    database: Optional[BaseModel]
    hyperparameters: Optional[BaseModel]
    experiment: Optional[BaseModel]
    training: Optional[BaseModel]
    compile: Optional[BaseModel]
