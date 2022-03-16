from yacmmal import autoconfig, BaseModel
from typing import List

class HyperParams(BaseModel):
    activation: str
    hidden_units: List[int]
    dropout: float

class ExperimentParams(BaseModel):
    test_size: float
    k_fold: int

@autoconfig(
        base_path="config/",
        config=[("hp_file", "hyperparameters", HyperParams),
                ("ep_file", "experiment", ExperimentParams)],
        format="yaml"
        )
def load_cfg(cfg):
    print(f"Config: {cfg}")
    print(f"Hyperparameters: {cfg.hyperparameters}")
    print(f"Experiment: {cfg.experiment}")

def main() -> int:
    load_cfg()
    return 0

if __name__ == "__main__":
    exit(main())

