from yacmmal import BaseModel
from yacmmal.load.yaml import YAMLLoader
from typing import List

class HyperParams(BaseModel):
    activation: str
    hidden_units: List[int]
    dropout: float

class ExperimentParams(BaseModel):
    test_size: float
    k_fold: int

def main() -> int:
    loader = YAMLLoader(base_path="config/")
    cfg = (
            loader
            .add_path("hp_file", "hyperparameters", HyperParams)
            .add_path("ep_file", "experiment", ExperimentParams)
            .extract()
            )
    print(f"Config: {cfg}")
    print(f"Hyperparameters: {cfg.hyperparameters}")
    print(f"Experiment: {cfg.experiment}")
    return 0

if __name__ == "__main__":
    exit(main())

