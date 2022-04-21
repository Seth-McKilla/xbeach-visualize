import netCDF4
import numpy as np
import matplotlib.pyplot as plt

f = netCDF4.Dataset('./xboutput.nc')

sediment_transport_x = f.variables['Susg']
print(sediment_transport_x.shape)