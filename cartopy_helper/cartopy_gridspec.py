import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.gridspec as gs


def make_grid(rows=0, cols=0, proj=ccrs.PlateCarree(), cbar=False):
    """Creates a list of axes for a figure with gridspec layout of
    pre-defined number of rows and columns

    Parameters:
    rows (int): Number of rows in grid
    cols (int): Number of columns in grid
    proj (cartopy.crs projection): cartopy.crs projection to be used
    cbar (Boolean): If True, will create extra column for colorbar
    to be placed in figure. Column will be the width of the other
    columns and height of total number of rows.

    Returns:
    axlist: List of axes for each individual figure in the grid.

    >>> make_grid(2,2,ccrs.PlateCarree(),cbar=True)
    [<AxesSubplot:>, <AxesSubplot:>, <AxesSubplot:>, <AxesSubplot:>, <AxesSubplot:>]

    >>> make_grid(2,2,ccrs.PlateCarree(),cbar=False)
    [<AxesSubplot:>, <AxesSubplot:>, <AxesSubplot:>, <AxesSubplot:>]
    """
    axlist = []
    fig2 = plt.figure(figsize=(20, 10))
    if cbar is False:
        spec2 = gs.GridSpec(ncols=cols, nrows=rows, figure=fig2)
        spec2.update(wspace=0.2, hspace=0.5)

        for x in range(rows):
            for y in range(cols):
                axlist.append(fig2.add_subplot(spec2[x, y]))
    else:
        spec2 = gs.GridSpec(ncols=cols + 1, nrows=rows, figure=fig2)

        for x in range(rows):
            for y in range(cols):
                axlist.append(fig2.add_subplot(spec2[x, y]))

        axlist.append(fig2.add_subplot(spec2[:, -1]))

    return axlist
