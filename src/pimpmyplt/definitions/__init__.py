from abc import ABC
from abc import abstractmethod
from typing import Any


class PimpRCParams(ABC):
    @abstractmethod
    def build(self) -> dict[str, Any]:
        raise NotImplementedError