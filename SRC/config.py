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
config_parameters['locationepsg'] = '4326' #  EPSG code

## The following parameters should not be changed  
config_parameters['gisdb'] = os.path.join(os.environ['HOME'], 'GRASSDATA') # path to the GRASSDATA folder
config_parameters['location'] = 'vaihingen'
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['locationepsg'] = '4326' #  EPSG code
config_parameters['outputfolder'] = '/home/tais/result'
config_parameters['inputdir'] = '/home/tais/data'
config_parameters['images_val'] = ['3','13','17','26','32','37']
config_parameters['images_classical_approach'] = ['1','5','7','11','15','21','23','28','30','34']
config_parameters['images_snorkel_approach'] = ['1','2','4','5','6','7','8','10','11','12','14','15','16','20','21','22','23','24','27','28','29','30','31','33','34','35','38']
config_parameters['images_snorkel_approach_unlabel'] = ['2','4','6','8','10','12','14','16','20','22','24','27','29','31','33','35','38']
config_parameters['images_snorkel_approach_gts'] = ['1','5','7','11','15','21','23','28','30','34']

## Please update the following paths according to your own configuration
data["dsm_folder"] = '/home/tais/data/ISPRS_semantic_labeling_Vaihingen/dsm'
data["top_folder"] = '/home/tais/data/ISPRS_semantic_labeling_Vaihingen/top'
data["gts_folder"] = '/home/tais/data/ISPRS_semantic_labeling_Vaihingen/gts_for_participants'
data["legend"] = '/home/tais/github/Legend.txt'
