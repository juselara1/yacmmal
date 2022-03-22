from yacmmal import BaseModel
from yacmmal.load.json import JSONLoader

class DBParams(BaseModel):
    hostname: str
    port: int
    user: str
    password: str
    database: str

class HyperParams(BaseModel):
    kernel: str
    gamma: float
    C: float

def main() -> int:
    loader = JSONLoader(base_path="config")
    cfg = (
        loader
        .add_path("hp_file", "hyperparameters", HyperParams)
        .add_path("db", "database", DBParams)
        .extract()
    )
    print(f"Config: {cfg}")
    print(f"Hyperparameters: {cfg.hyperparameters}")
    print(f"Database: {cfg.database}")
    return 0

if __name__ == "__main__":
    exit(main())
