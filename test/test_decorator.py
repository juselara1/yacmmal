from traceback import format_exception_only
from yacmmal import autoconfig, BaseModel
from typing import List
import pytest


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


class TestDecorator:
    @pytest.mark.parametrize("format", [("yaml"), ("json")])
    def test_config_attrs(self, format: str):
        @autoconfig(
            base_path=f"test/config/{format}/",
            config=[
                ("hp_file", "hyperparameters", HyperParams),
                ("cp_file", "compile", CompileParams),
                ("db_file", "database", DBParams),
                ("ep_file", "experiment", ExperimentParams),
                ("tp_file", "training", TrainParams),
            ],
            format=format,
        )
        def config_attrs(self, cfg):
            assert hasattr(cfg, "hyperparameters")
            assert hasattr(cfg, "compile")
            assert hasattr(cfg, "database")
            assert hasattr(cfg, "experiment")
            assert hasattr(cfg, "training")

    @pytest.mark.parametrize("format", [("yaml"), ("json")])
    def test_config_instances(self, format: str):
        @autoconfig(
            base_path=f"test/config/{format}/",
            config=[
                ("hp_file", "hyperparameters", HyperParams),
                ("cp_file", "compile", CompileParams),
                ("db_file", "database", DBParams),
                ("ep_file", "experiment", ExperimentParams),
                ("tp_file", "training", TrainParams),
            ],
            format=format,
        )
        def config_instances(cfg):
            assert isinstance(cfg.hyperparameters, HyperParams)
            assert isinstance(cfg.compile, CompileParams)
            assert isinstance(cfg.database, DBParams)
            assert isinstance(cfg.experiment, ExperimentParams)
            assert isinstance(cfg.training, TrainParams)
