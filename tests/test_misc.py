import pytest

import pimpmyplt


def test_compose_raises() -> None:
    with pytest.raises(TypeError):
        pimpmyplt.compose([1, "?"])  # type: ignore
