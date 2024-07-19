"""Utility functions for working with Cartopy"""

import cartopy.feature as cfeature
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt

def default_map(ax,extent=None,scale='110m',ec='k',lw=0.75):
    """Draw basic features onto a map

    Parameters
    ----------
    ax : cartopy.mpl.geoaxes.GeoAxes
        Target axis for drawing features

    extent : list, default = [-130,-65,25,55]
        Map extent in [minlon,maxlon,minlat,maxlat] passed to ax.set_extent

    scale : str, default = '110m'
        Scale of drawn features. Options: ['10m', '50m', '110m']
    """

    if extent is None:
        extent = [-130,-65,25,55]

    ax.set_extent(extent,crs=ccrs.PlateCarree())
    
    ax.add_feature(cfeature.BORDERS.with_scale(scale), ec=ec, fc="none", lw=lw)
    ax.add_feature(cfeature.LAKES.with_scale(scale), ec=ec, fc="none", lw=lw)
    ax.add_feature(cfeature.STATES.with_scale(scale),ec=ec,fc='none',lw=lw)
    ax.add_feature(cfeature.OCEAN.with_scale(scale),ec=ec,fc='none',lw=lw) 

    return None

def map_tiles(ax,zoom=None):
    """Add open street map tiles to a map

    Parameters
    ----------
    ax : cartopy.mpl.geoaxes.GeoAxes
        Target axis for drawing features

    zoom : int, default = None
        Zoom level for the map. 
    """

    if zoom is None:
        raise ValueError("Need to specify a zoom level")

    tiles = cimgt.OSM(cache=True)
    ax.add_image(tiles, zoom, interpolation="spline36", regrid_shape=2000)

    return None