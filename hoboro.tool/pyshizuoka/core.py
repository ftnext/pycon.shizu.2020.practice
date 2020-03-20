from dataclasses import dataclass


@dataclass(frozen=True)
class Session:
    title: str
    speaker: str
    level: str
    category: str
    url: str
    content: str
