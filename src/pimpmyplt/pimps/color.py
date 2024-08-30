from dataclasses import dataclass
from typing import Any
from typing import Literal

from cycler import cycler

from pimpmyplt.pimps.abc import Pimper

_COLORS_NORMAL = [
    "#122a55",
    "#693d73",
    "#b55379",
    "#ee7a6c",
    "#ffb55f",
    "#f9f871",
]
_GRAYS_NORMAL = [
    "#b0b0b0",
    "#dedede",
]
_COLORS_LIGHT = [
    "#122a55",
    "#b59fba",
    "#dbaabc",
    "#f7bdb6",
    "#ffdab0",
    "#fcfcb8",
]
_GRAY_LIGHT = [
    "#d8d8d8",
    "#efefef",
]

_OPTIONS = {
    "normal": _COLORS_NORMAL,
    "light": _COLORS_LIGHT,
    "gray_normal": _GRAYS_NORMAL,
    "gray_light": _GRAY_LIGHT,
}


@dataclass(kw_only=True, frozen=True)
class PimpColorPredefined(Pimper):
    mode: Literal["normal", "light", "gray_normal", "gray_light"] = "normal"

    def __post_init__(self) -> None:
        if self.mode not in _OPTIONS:
            msg = f"Unknown predefined color set with name '{self.mode}'"
            raise ValueError(msg)

    def build(self) -> dict[str, Any]:
        return {"axes.prop_cycle": cycler(color=_OPTIONS[self.mode])}
