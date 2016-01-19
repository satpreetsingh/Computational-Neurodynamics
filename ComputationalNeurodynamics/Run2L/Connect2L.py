"""
Computational Neurodynamics
Exercise 2

(C) Murray Shanahan et al, 2015
"""

from HHNetwork import HHNetwork
import numpy as np
import numpy.random as rn


def Connect2L(N0, N1):
  """
  Constructs two layers of Izhikevich neurons and connects them together.
  Layers are arrays of N neurons. Parameters for regular spiking neurons
  extracted from:

  http://www.izhikevich.org/publications/spikes.htm
  """

  F = 50/np.sqrt(N1)  # Scaling factor
  D = 5               # Conduction delay
  Dmax = 10           # Maximum conduction delay

  net = HHNetwork([N0, N1], Dmax)

  # Neuron parameters
  # Each layer comprises a heterogenous set of neurons, with a small spread
  # of parameter values, so that they exhibit some dynamical variation
  # (To get a homogenous population of canonical "regular spiking" neurons,
  # multiply r by zero.)

  # Layer 0 (regular spiking)
  r = rn.rand(N0)
  net.layer[0].N = N0

  # Layer 1 (regular spiking)
  r = rn.rand(N1)
  net.layer[1].N = N1

  for i in range(0, 2):
    net.layer[i].gNa = 555.0 + 445*(r**2)
    net.layer[i].gK = 21.0 +16*(r**2)
    net.layer[i].gL = 0.075 +0.275*(r**2)
    net.layer[i].ENa = 655.5 + 544.5*(r**2)
    net.layer[i].EK = -6.0 + 8*(r**2)
    net.layer[i].EL = 92.5 +87.5*(r**2)
    net.layer[i].C = 2.5 + 2.5*(r**2)

    net.layer[i].Ik = 0.0*np.ones(N0)
    net.layer[i].m = 0.0*np.ones(N0)
    net.layer[i].n = 0.0*np.ones(N0)
    net.layer[i].h = 0.0*np.ones(N0)
    net.layer[i].alpham = 0.0*np.ones(N0)
    net.layer[i].alphan = 0.0*np.ones(N0)
    net.layer[i].alphah = 0.0*np.ones(N0)
    net.layer[i].betam = 0.0*np.ones(N0)
    net.layer[i].betan = 0.0*np.ones(N0)
    net.layer[i].betah = 0.0*np.ones(N0)


  ## Connectivity matrix (synaptic weights)
  # layer[i].S[j] is the connectivity matrix from layer j to layer i
  # S(i,j) is the strength of the connection from neuron j to neuron i
  net.layer[1].S[0]      = np.ones([N1, N0])
  net.layer[1].factor[0] = F
  net.layer[1].delay[0]  = D * np.ones([N1, N0], dtype=int)

  return net