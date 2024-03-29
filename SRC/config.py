#!/usr/bin/env python

"""
This script is used to store all configuration parameter to run the main code (jupyter notebook)

"""

import os

# Initialize dictionnaries
config_parameters = {}
data = {}

## Please update the following paths according to your own configuration
config_parameters['GISBASE'] = '/usr/lib/grass78'
config_parameters['PYTHONLIB'] = '/usr/bin/python3'
#config_parameters['GDAL_DATA'] = 'C:/OSGeo4W64/share/epsg_csv' #For EPSG csv files

## The following parameters should not be changed  
config_parameters['gisdb'] = os.path.join(os.environ['HOME'], 'GRASSDATA') # path to the GRASSDATA folder
config_parameters['location'] = 'flair-one'
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['locationepsg'] = '2154' #  EPSG code
config_parameters['outputfolder'] = os.path.join(os.environ['HOME'], 'result')
config_parameters['inputdir'] = os.path.join(os.environ['HOME'], 'data')
data["legend"] = os.path.join(os.environ['HOME'], 'github', 'Legend.txt')