import pytest
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.rcsetup import cycler

import pimpmyplt
from pimpmyplt.pimps import PimpFigSizeDIN
from pimpmyplt.pimps import PimpSaveFigPDF
from pimpmyplt.pimps import PimpSaveFigPNG
from pimpmyplt.pimps import PimpTightLayout
from pimpmyplt.pimps import PimpUseTeX
from pimpmyplt.pimps.figsize import PimpFigSizeCustom
from pimpmyplt.pimps.text import PimpText


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
    collections = pimpmyplt.compose([PimpFigSizeDIN(din_format="A6", mode="landscape")])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_figsize_A3P() -> Figure:
    collections = pimpmyplt.compose([PimpFigSizeDIN(din_format="A3", mode="portrait")])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_figsize_custom() -> Figure:
    collections = pimpmyplt.compose([PimpFigSizeCustom(width=12, height=2)])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_usetex() -> Figure:
    collections = pimpmyplt.compose([PimpUseTeX()])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_tightlayout() -> Figure:
    collections = pimpmyplt.compose([PimpTightLayout()])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_tightlayout_plus_figsize_A6L() -> Figure:
    collections = pimpmyplt.compose(
        [
            PimpTightLayout(),
            PimpFigSizeDIN(din_format="A6", mode="landscape"),
        ],
    )
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_savefig_PNG_highQ() -> Figure:
    collections = pimpmyplt.compose([PimpSaveFigPNG(dpi=400)])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_savefig_PDF_highQ() -> Figure:
    # This will be a PNG anyway, because the test framework does not support PDF
    collections = pimpmyplt.compose([PimpSaveFigPDF()])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_custom_compose() -> Figure:
    custom = {
        "lines.linewidth": 10,
        "lines.linestyle": "--",
        "axes.prop_cycle": cycler(color=["r", "g", "b", "y"]),
    }
    collections = pimpmyplt.compose([custom, PimpUseTeX()])
    plt.rcParams.update(collections)
    return plot()


@pytest.mark.mpl_image_compare
def test_text() -> Figure:
    collections = pimpmyplt.compose([PimpText(size=30)])
    plt.rcParams.update(collections)
    return plot()
