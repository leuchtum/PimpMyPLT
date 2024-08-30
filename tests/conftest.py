from typing import Generator

import matplotlib as mpl
import pytest


@pytest.fixture(autouse=True)
def _reset_matplotlib_before_and_after_use() -> Generator[None, None, None]:
    mpl.rcdefaults()
    yield
    mpl.rcdefaults()
