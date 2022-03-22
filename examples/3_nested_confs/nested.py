from yacmmal import autoconfig, BaseModel
from yacmmal.types.config import Config
from typing import List

class NNParams(BaseModel):
    activation: str
    hidden_units: List[int]
    dropout: float

class SVMParams(BaseModel):
    kernel: str
    gamma: float
    C: float

class HyperParams(BaseModel):
    neural_network: NNParams
    svm: SVMParams

class MySQL(BaseModel):
    host: str
    port: int
    user: str
    database: str

class PostgreSQL(BaseModel):
    host: str
    port: int
    user: str
    database: str

class DBParams(BaseModel):
    mysql: MySQL
    postgresql: PostgreSQL

class Config(BaseModel):
    hyperparams: HyperParams
    database: DBParams

@autoconfig(
        base_path="config/",
        config=[
            ("hparams", "hyperparameters", HyperParams),
            ("database", "database", DBParams)
            ],
        format="toml"
        )
def main(cfg: Config) -> int:
    print(cfg)
    print(cfg.database.mysql)
    return 0

if __name__ == "__main__":
    exit(main())
