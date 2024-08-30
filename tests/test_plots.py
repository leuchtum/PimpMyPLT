import pytest
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.rcsetup import cycler

import pimpmyplt as pimp


def plot() -> Figure:
    fig, ax = plt.subplots()
    x = range(100)
    y = [i**2 for i in x]
    ax.plot(x, y)
    ax.set_title(r"Title")
    ax.set_xlabel(r"x")
    ax.set_ylabel(r"y")
    return fig


@pytest.mark.mpl_image_compare
def test_figsize_A6L() -> Figure:
    collections = pimp.compose([pimp.PimpFigSizeDINA(din_number=6, mode="landscape")])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_figsize_A3P() -> Figure:
    collections = pimp.compose([pimp.PimpFigSizeDINA(din_number=3, mode="portrait")])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_usetex() -> Figure:
    collections = pimp.compose([pimp.PimpUseTeX()])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_tightlayout() -> Figure:
    collections = pimp.compose([pimp.PimpTightLayout()])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_tightlayout_plus_figsize_A6L() -> Figure:
    collections = pimp.compose(
        [pimp.PimpTightLayout(), pimp.PimpFigSizeDINA(din_number=6, mode="landscape")],
    )
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_savefig_PNG_highQ() -> Figure:
    collections = pimp.compose([pimp.PimpSaveFig(format="png", dpi=400)])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_savefig_PDF_highQ() -> Figure:
    # This will be a PNG anyway, because the test framework does not support PDF
    collections = pimp.compose([pimp.PimpSaveFig(format="pdf", dpi=400)])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_custom_compose() -> Figure:
    custom = {
        "lines.linewidth": 10,
        "lines.linestyle": "--",
        "axes.prop_cycle": cycler(color=["r", "g", "b", "y"]),
    }
    collections = pimp.compose([custom, pimp.PimpUseTeX()])
    plt.rcParams.update(collections)
    return plot()
