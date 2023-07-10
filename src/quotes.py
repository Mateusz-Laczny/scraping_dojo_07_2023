from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class Quote:
    by: str
    text: str
    tags: list[str]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
