# User Guide

The `yacmmal` package can be used in two main modes:

## Decorator

The decorator mode allows to extract configurations in a single function. For instance, suppose that you have a project with the following structure:

```sh
.
├── config
│   ├── ep_file.yaml
│   └── hp_file.yaml
└── main.py
```

* `hp_file.yaml` contains the hyperparameters for your model:

```yaml
activation: "relu"
hidden_units:
  - 32
  - 64
dropout: 0.2
```

* `ep_file.yaml` contains the experiment parameters:

```yaml
test_size: 0.3
k_fold: 5
```

You can easily load these parameters into a single `Config` object using a decorated function:

```python
# main.py
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
    print(cfg)
    ...
```

The `autoconfig` decorator defines:

* `base_path`: for the root path of the config files.
* `config`: a sequence of tuples, such that each tuple contains three elements `(file_name, config_type, dataclass)`. You can select between `{"database", "hyperparameters", "experiment", "training", "compile"}` for `config_type`
* `format`: the file format of the config files (e.g, `yaml`).

> You can find this example in `examples/decorator.py`

## Builder API

The builder API allows to dynamically build a `Config` object, using the `yacmmal`'s loaders. For example, suppose that you have a project with the same structure and `yamls` that were used in the `decorator` example, you can create the configuration object as follows:

```python
# main.py
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

loader = YAMLLoader(base_path="config/")
cfg = (
        loader
        .add_path("hp_file", "hyperparameters", HyperParams)
        .add_path("ep_file", "experiment", ExperimentParams)
        .extract()
        )
print(f"Config: {cfg}")

```

* The `yacmmal.load.base.Loader` is initialized with the `base_path` of the configuration files.
* The `add_path` method receives:
    * `path`: file name for the configuration.
    * `name`: configuration type in `{"database", "hyperparameters", "experiment", "training", "compile"}`
    * `dclass`: dataclass used to extract the configurations.
* The `extract` method generates a `Config` object with the consolidated consolidations.

> You can find this example in `examples/builder.py`
