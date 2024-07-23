"""Utility functions for working with cartopy projections"""

import cartopy.crs as ccrs
import geopandas as gpd
import shapely


def proj_transform(point_start, proj_final, proj_start=ccrs.PlateCarree()):
    """Perform a coordinate transformation for a point between two projections

    Parameters
    ----------

    point_start : array_like
        Sequence like [x0, y0] representing the ordered pair in the original
        coordinate system

    proj_final : cartopy.crs
        Map projection which will be used as the target projection for the
        resulting coordinate transformation

    proj_start : optional, default=cartopy.crs.PlateCarree()
        Map projection corresponding to `point_start`; assumed to be Plate
        Carree (longitude, latitude)

    Returns
    -------

    point_final : array_like
        Sequence like [xf, yf] representing the ordered pair in the projected
        coordinate system

    """

    x0, y0 = point_start

    pt_start = gpd.GeoDataFrame(geometry=[shapely.Point(x0, y0)], crs=proj_start)

    pt_final = pt_start.to_crs(proj_final)

    xf = pt_final["geometry"].iloc[0].x
    yf = pt_final["geometry"].iloc[0].y

    point_final = (xf, yf)

    return point_final


def projected_extent(extents, proj):
    """Calculate extent in projected coordinates based on lat/lon bounding box

    Take bounding box in latitude / longitude coordinates and convert to a
    complimentary bounding box in the projected coordinate system. The new
    bounding box will be aligned with the axes of the projected coordinate
    system

    Parameters
    ----------

    extents : array_like
        Sequence like [minlon, minlat, maxlon, maxlat] representing the
        desired bounding box in latitude / longitude coordinates

    proj : cartopy.crs
        Map projection which will be used as the target projection for the
        resulting bounding box limits.

    Returns
    -------

    extents_projected : array_like
        Sequence like [xmin, ymin, xmax, ymax] representing the desired
        bounding box in the projected coordinates
    """

    x0, y0, x1, y1 = extents

    bbox = {
        "bounding box": shapely.Polygon(
            shell=[(x0, y0), (x0, y1), (x1, y1), (x1, y0), (x0, y0)]
        )
    }

    bbox_latlon = gpd.GeoDataFrame(geometry=list(bbox.values()), crs=ccrs.PlateCarree())

    bbox_projected = shapely.envelope(bbox_latlon.to_crs(proj))

    xx, yy = bbox_projected.geometry.iloc[0].boundary.coords.xy

    extents_projected = [min(xx), min(yy), max(xx), max(yy)]

    return extents_projected
