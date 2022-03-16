from pydantic import BaseModel
from typing import Protocol, Union, Dict

class DataClass(Protocol):
    __dataclass_fields__: Dict

TDataClass = Union[DataClass, BaseModel]
