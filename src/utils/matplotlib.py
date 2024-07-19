"""Utility functions for working with Matplotlib"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def discrete_colorbar(
    vmin,
    vmax,
    dlev=None,
    cmap_name="inferno",
    set_bad=None,
    set_over=None,
    set_under=None,
    display_boundaries=False,
    display_colorbar=False,
):
    """Make a discrete colorbar based on specified range and step size

    Parameters
    ----------
    vmin : int or float
        lower boundary for colorbar

    vmax : int or float
        upper boundary for colorbar

    dlev : int or float, default = None
        spacing between color bounds. If None, spacing is chosen to give a
        colorbar with 12 evenly-spaced colors

    cmap_name : str, default = 'inferno'
        Name pointing to a Matplotlib colormap. For default options, see
        https://matplotlib.org/stable/users/explain/colors/colormaps.html

    set_bad : str, default = None
        Fill color to use for NaN values

    set_over : str, default = None
        Fill color to use for values greater than vmax.

    set_under : str, default = None
        Fill color to use for values less than vmin

    display_boundaries : bool, default = False
        if True, printout the boundaries between colors

    display_colorbar : bool, default = False
        if True, generate a plot to display the colorbar

    Returns
    ----------
    smap : matplotlib.cm.ScalarMappable
        Object used to map data to desired colormap. Can access the underlying
        colormap with `smap.cmap` and the underlying norm with `smap.norm`
    """

    if dlev is None:
        dlev = np.diff(np.linspace(vmin, vmax, 12))[0]

    cmap_boundaries = np.arange(vmin, vmax + dlev / 2, dlev)

    cmap = mpl.colormaps[cmap_name]

    if set_bad is not None:
        cmap.set_bad(set_bad)

    if set_under is not None:
        cmap.set_under(set_under)

    if set_over is not None:
        cmap.set_over(set_over)

    norm = mpl.colors.BoundaryNorm(ncolors=cmap.N, boundaries=cmap_boundaries)
    smap = mpl.cm.ScalarMappable(cmap=cmap, norm=norm)

    if display_boundaries:
        print(cmap_boundaries)

    if display_colorbar:
        fig, ax = plt.subplots(figsize=(6, 0.3))
        fig.colorbar(smap, cax=ax, orientation="horizontal")
        plt.show()

    return smap
