"""Utility functions for working with cartopy projections"""

import cartopy.crs as ccrs
import geopandas as gpd
import shapely


def proj_transform(point_start,proj_final,proj_start=ccrs.PlateCarree()):
    """Perform a coordinate transformation for a point between two projections"""

    x0,y0 = point_start

    pt_start = gpd.GeoDataFrame(
        geometry = [shapely.Point(x0,y0)],
        crs=proj_start
    )

    pt_final = pt_start.to_crs(proj_final)

    xf = pt_final['geometry'].iloc[0].x
    yf = pt_final['geometry'].iloc[0].y

    return (xf,yf)

