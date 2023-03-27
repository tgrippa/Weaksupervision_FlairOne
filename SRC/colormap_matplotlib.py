#!/usr/bin/env python


import matplotlib as mpl
	
def Colormap(colors_list=['black','red','yellow','green','cyan','grey'], boundaries=[-1.0,1.0, 2.0, 3.0, 4.0, 5.0]):
	'''
	Function returning cmap colormap for matplotlib 
	'''
	# Custom color map for ploting label using matplotlib
	cmap_label = mpl.colors.ListedColormap(colors_list)
	norm_label = mpl.colors.BoundaryNorm(boundaries, cmap_label.N, clip=True)
	return cmap_label,norm_label

