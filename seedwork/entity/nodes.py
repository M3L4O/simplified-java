from dataclasses import dataclass, field


@dataclass
class Node:
    line: int
    column: int
    code: str
    type: int | float | bool | str | None = field(default=None)
    value: int | float | bool | str | None = field(default=None)
