import netCDF4
import numpy as np
import matplotlib.pyplot as plt

f = netCDF4.Dataset('./xboutput.nc')

print(f.variables.keys())
