from typing import Any

from pimpmyplt.definitions import PimpRCParams


class PimpUseTeX(PimpRCParams):
    def build(self) -> dict[str, Any]:
        return {
            "text.usetex": True,
            "font.family": "serif",
            "font.serif": "cm",
        }
