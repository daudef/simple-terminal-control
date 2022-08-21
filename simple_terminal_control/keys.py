from abc import ABC
from dataclasses import KW_ONLY, dataclass
from enum import Enum
from typing import TypeAlias

from simple_terminal_control.position import TerminalPosition


@dataclass(frozen=True, kw_only=True)
class Delete:
    alt: bool


class Tab:
    pass


class Enter:
    pass


@dataclass(frozen=True)
class Arrow:
    class Direction(Enum):
        UP = 0
        DOWN = 1
        RIGHT = 2
        LEFT = 3

    direction: Direction
    _: KW_ONLY
    shift: bool
    alt: bool


@dataclass(frozen=True)
class _MouseBase(ABC):
    position: TerminalPosition
    _: KW_ONLY
    shift: bool
    ctrl: bool


@dataclass(frozen=True, kw_only=True)
class Click(_MouseBase):
    secondary: bool


@dataclass(frozen=True, kw_only=True)
class Drag(_MouseBase):
    secondary: bool
    origin: TerminalPosition


@dataclass(frozen=True, kw_only=True)
class Scroll(_MouseBase):
    down: bool


Key: TypeAlias = Delete | Tab | Enter | Arrow | Click | Drag | Scroll
