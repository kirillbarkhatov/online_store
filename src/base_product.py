from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный класс для класса Product и его подклассов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Общий функционал для всех подклассов"""
        pass
