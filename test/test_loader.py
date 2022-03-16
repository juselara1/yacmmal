from yacmmal.load.yaml import YAMLLoader
from yacmmal import BaseModel
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

class TestYAMLLoader:
    yaml_loader = YAMLLoader(base_path="test/config/")
    config = (
            yaml_loader
            .add_path(
                path="hp_file",
                name="hyperparameters",
                dclass=HyperParams
                )
            .add_path(
                path="cp_file",
                name="compile",
                dclass=CompileParams
                )
            .add_path(
                path="db_file",
                name="database",
                dclass=DBParams
                )
            .add_path(
                path="ep_file",
                name="experiment",
                dclass=ExperimentParams
                )
            .add_path(
                path="tp_file",
                name="training",
                dclass=TrainParams
                )
            .extract()
            )

    def test_config_attrs(self):
        assert hasattr(self.config, "hyperparameters")
        assert hasattr(self.config, "compile")
        assert hasattr(self.config, "database")
        assert hasattr(self.config, "experiment")
        assert hasattr(self.config, "training")

    def test_config_instances(self):
        assert isinstance(self.config.hyperparameters, HyperParams)
        assert isinstance(self.config.compile, CompileParams)
        assert isinstance(self.config.database, DBParams)
        assert isinstance(self.config.experiment, ExperimentParams)
        assert isinstance(self.config.training, TrainParams)
