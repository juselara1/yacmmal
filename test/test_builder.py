from yacmmal.load.yaml import YAMLLoader
from yacmmal.load.json import JSONLoader
from yacmmal import BaseModel
from typing import Callable, List
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


class TestBuilder:
    @staticmethod
    def setup_loader(loader: Callable, path: str):
        config_loader = loader(base_path=f"test/config/{path}/")
        config = (
            config_loader.add_path(
                path="hp_file", name="hyperparameters", dclass=HyperParams
            )
            .add_path(path="cp_file", name="compile", dclass=CompileParams)
            .add_path(path="db_file", name="database", dclass=DBParams)
            .add_path(path="ep_file", name="experiment", dclass=ExperimentParams)
            .add_path(path="tp_file", name="training", dclass=TrainParams)
            .extract()
        )
        return config

    @pytest.mark.parametrize(
        "loader, path", [(YAMLLoader, "yaml"), (JSONLoader, "json")]
    )
    def test_config_attrs(self, loader: Callable, path: str):
        config = TestBuilder.setup_loader(loader=loader, path=path)
        assert hasattr(config, "hyperparameters")
        assert hasattr(config, "compile")
        assert hasattr(config, "database")
        assert hasattr(config, "experiment")
        assert hasattr(config, "training")

    @pytest.mark.parametrize(
        "loader, path", [(YAMLLoader, "yaml"), (JSONLoader, "json")]
    )
    def test_config_instances(self, loader, path):
        config = TestBuilder.setup_loader(loader=loader, path=path)
        assert isinstance(config.hyperparameters, HyperParams)
        assert isinstance(config.compile, CompileParams)
        assert isinstance(config.database, DBParams)
        assert isinstance(config.experiment, ExperimentParams)
        assert isinstance(config.training, TrainParams)
