import numpy as np

def solve(t1, t2):
    """ Substitute values in solutions of ellipse
    equations to localize users.

    For details on where these equations come from, 
    go to notebooks folder and see `localizer.ipynb`.

    Parameters
    ----------
    tof1: float
        TOF of receive antenna 1.

    tof2: float
        TOF of receieve antenna 2.

    Returns
    -------
    coordinates: tuple
        First element denotes x-coordinate and second y-coordinate
    """

    x1 = -(t1 - t2)*(t1 + t2)/4.0
    y1 = -np.sqrt(-(t1 - t2 - 2)*(t1 - t2 + 2)*(t1 + t2 - 2)*(t1 + t2 + 2))/4.0
    x2 = -(t1 - t2)*(t1 + t2)/4.0
    y2 = np.sqrt(-(t1 - t2 - 2)*(t1 - t2 + 2)*(t1 + t2 - 2)*(t1 + t2 + 2))/4.0

    # If y is negative, the solution is incorrect. Practically, this is because
    # negative y can't be in LOS of antenna. So, discard that.
    if y1 < 0:
        return (x2, y2)
    else:
        return (x1, y1)

    return coordinates
    