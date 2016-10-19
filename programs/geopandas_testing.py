import numpy as np
import pandas as pd
import geopandas as gp
import os
import subprocess
import pylab as pl

# make sure we are at the top of the repo
wd = subprocess.check_output('git rev-parse --show-toplevel', shell = True)
os.chdir(wd[:-1]) #-1 removes \n

# read in nyc shapefiles
nycshp = gp.read_file('data/nycb2010_16c/nycb2010.shp')

# we only need manhattan 
manshp = nycshp[nycshp.BoroName == 'Manhattan']

# read in LEHD OD data
lehd = pd.read_csv('data/lehd_od_2014.csv',
 dtype = {'w_geocode':'string',
          'h_geocode':'string'})

# clean LEHD geocodes to match census blocks from nyc shp
lehd['w_geo'] = lehd['w_geocode'].str[4:]
lehd['h_geo'] = lehd['h_geocode'].str[4:]

# prepare manhattan data for merge
manshp['w_geo'] = manshp['BCTCB2010']
manshp['h_geo'] = manshp['BCTCB2010']

# merge on home geocode

home = manshp.merge(lehd, on = 'h_geo')
