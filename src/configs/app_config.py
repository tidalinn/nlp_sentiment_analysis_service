from pathlib import Path
from typing import Union

from omegaconf import OmegaConf
from pydantic import BaseModel, ConfigDict


class BaseValidatedConfig(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
        protected_namespaces=()
    )


class AppConfig(BaseValidatedConfig):
    vocabulary_simple: dict[str, list[str]]

    @classmethod
    def from_yaml(cls, path: Union[str, Path]) -> 'AppConfig':
        config = OmegaConf.to_container(OmegaConf.load(path), resolve=True)
        return cls(**config)
