from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
import pylab
import numpy as np

import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D
from math import sin
from math import cos

def inputs():
	B = float(input('Enter the magnetic field strength in the X direction:  '))
	E = float(input('Enter the electric field strength in the Z direction:  '))
	m = float(input('Enter the mass of the particle:  '))
	Q = float(input('Enter the charge of the particle:  '))
	time = input('Enter your desired length of time:  ')
	print "The particle will start at rest at the origin of a cyclotron"

	return B, E, m, Q, time


def position(B, E, m, Q, time):

	x = []
	y = []
	z = []
	t = np.arange(0, time, 0.00001).tolist()
	w = Q * B / m
	i = 1

	while i < len(t):
		currentTime = t[i]
		wt = w*currentTime
		currentPositionY = (E / (w * B)) * (wt - sin(wt))
		currentPositionZ = (E / (w * B)) * (1 - cos(w*t[i]))
		x.append(0)
		y.append(currentPositionY)
		z.append(currentPositionZ)

		i += 1
	return x, y, z, t

def plotting(x, y, z, t):
	fig = pylab.figure()
	ax = Axes3D(fig)
	
	ax.plot(x, y, z)
	pl.xlabel('X Position')
	pl.ylabel('Y Position')
	pl.title('Position of a Particle ')
	pl.show()

def main():
	B, E, m, Q, time = inputs()
	x, y, z, t = position(B, E, m, Q, time)
	plotting(x, y, z, t)




if __name__=='__main__':
	main()