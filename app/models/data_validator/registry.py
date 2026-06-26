from typing import Any, Callable, TypeVar

T = TypeVar("T")
CLASS_REGISTRY: dict[str, Any] = {}


def register(name: str | None = None) -> Callable[[type[T]], type[T]]:
    def wrapper(cls: type[T]) -> type[T]:
        CLASS_REGISTRY[name or cls.__name__] = cls
        return cls

    return wrapper
