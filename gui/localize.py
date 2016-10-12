import numpy as np

def solve(tof1, tof2):
	""" Substitute values in solutions of ellipse
	equations to localize users.

	For details on where these equations come from, 
	go to notebooks folder and see `localizer.ipynb`.

	Parameters
	----------
	tof1: float array
		TOFs of receive antenna 1.

	tof2: float array
		TOFs of receieve antenna 2.

	Returns
	-------
	coordinates: list of tuples
		First element denotes x-coordinate and second y-coordinate
	"""

	coordinates = []

	for t1, t2 in zip(tof1, tof2):
		x1 = -(t1 - t2)*(t1 + t2)/4.0
		y1 = -np.sqrt(-(t1 - t2 - 2)*(t1 - t2 + 2)*(t1 + t2 - 2)*(t1 + t2 + 2))/4.0
		x2 = -(t1 - t2)*(t1 + t2)/4.0
		y2 = np.sqrt(-(t1 - t2 - 2)*(t1 - t2 + 2)*(t1 + t2 - 2)*(t1 + t2 + 2))/4.0

		# If y is negative, the solution is incorrect. Practically, this is because
		# negative y can't be in LOS of antenna. So, discard that.
		if y1 < 0:
			coordinates.append((x2, y2))
		else:
			coordinates.append((x2, y2))

	return coordinates