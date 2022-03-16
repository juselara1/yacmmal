from yacmmal import autoconfig, BaseModel 
from typing import List

class HyperParams(BaseModel):
    activation: str
    hidden_units: List[int]
    dropout: float

class CompileParams(BaseModel):
    learning_rate: float
    loss: str
    optimizer: str
    metrics: List[str]

class DBParams(BaseModel):
    host: str
    port: int
    db: str
    user: str

class ExperimentParams(BaseModel):
    test_size: float
    k_fold: int

class TrainParams(BaseModel):
    epochs: int
    batch_size: int

@autoconfig(
        base_path="test/config/",
        config=[
            ("hp_file", "hyperparameters", HyperParams),
            ("cp_file", "compile", CompileParams),
            ("db_file", "database", DBParams),
            ("ep_file", "experiment", ExperimentParams),
            ("tp_file", "training", TrainParams)
            ],
        format="yaml"
        )
def test_config_attrs(cfg):
    assert hasattr(cfg, "hyperparameters")
    assert hasattr(cfg, "compile")
    assert hasattr(cfg, "database")
    assert hasattr(cfg, "experiment")
    assert hasattr(cfg, "training")

@autoconfig(
        base_path="test/config/",
        config=[
            ("hp_file", "hyperparameters", HyperParams),
            ("cp_file", "compile", CompileParams),
            ("db_file", "database", DBParams),
            ("ep_file", "experiment", ExperimentParams),
            ("tp_file", "training", TrainParams)
            ],
        format="yaml"
        )
def test_config_instances(cfg):
    assert isinstance(cfg.hyperparameters, HyperParams)
    assert isinstance(cfg.compile, CompileParams)
    assert isinstance(cfg.database, DBParams)
    assert isinstance(cfg.experiment, ExperimentParams)
    assert isinstance(cfg.training, TrainParams)
