from dataclasses import dataclass


@dataclass
class Quote:
    author: str
    quote_text: str
    tags: list[str]