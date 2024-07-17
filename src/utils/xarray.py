"""Utility functions for working with xarray data types"""


def display_vars(dset, var_dsec="var_desc"):
    """Displays variables, units, and descriptions of an xarray dataset

    Generates a printout of each variable within dset that includes the
    variable name, the units, and an extended description of the variable (if
    available).

    Parameters
    ----------
    dset : xarray.Dataset
        Target dataset. It is possible to call `display_vars` on an unformatted
        `dset` e.g., display_vars(xr.open_dataset(file)), or on a formatted
        `dset` e.g., display_vars(get_cmaq_metadata(xr.open_dataset(file))).

    var_dsec : string, default='var_desc'
        Name of the attribute for the xarray.DataArray instances within `dset`
        which contains a description of the variable

    Returns
    -------
    None

    See Also
    -------
    cmaq.get_cmaq_metadata
    """

    var = "VARNAME"
    units = "UNITS"
    desc = "DESCRIPTION"

    print("-" * 80)
    print(f"| {var:16} | {units:16} | {desc}")
    print("-" * 80)

    ct = 1
    for var in list(dset.data_vars):
        desc = ""
        units = ""

        try:
            desc = getattr(dset[var], var_dsec)
        except Exception:
            pass

        try:
            units = dset[var].units
        except Exception:
            pass

        print(f"| {var:16} | {units:16} | {desc}")

        if ct % 6 == 0:
            print("-" * 80)

        ct += 1

    return None
