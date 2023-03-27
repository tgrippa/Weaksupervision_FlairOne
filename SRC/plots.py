#!/usr/bin/env python

"""
Functions for plotting learning curves (loss, val_loss) and scatterplot for regression task
"""

import matplotlib.pyplot as plt
import numpy as np
import os

def plot_loss(history, save_path, ylim=[0,25.0], show=False):
    fig = plt.subplots(figsize=(15, 9))
    plt.plot(history.history["loss"])
    plt.plot(history.history["val_loss"])
    plt.title("The loss curve of training and test datasets")
    plt.legend(['train', 'val'], loc='upper left')
    plt.ylabel("loss")
    plt.xlabel("epoch")
    plt.ylim(ylim)
    plt.savefig(save_path, dpi = 300)
    if show:
        plt.show()
    else: 
        plt.close()
        
def plot_accuracy(history, save_path, ylim=[0,25.0], show=False):
	fig = plt.subplots(figsize=(15, 9))
	plt.plot(history.history["accuracy"])
	plt.plot(history.history["val_accuracy"])
	plt.title("The accuracy curve of training and test datasets")
	plt.legend(['train', 'val'], loc='upper left')
	plt.ylabel("accuracy")
	plt.xlabel("epoch")
	plt.ylim(ylim)
	plt.savefig(save_path, dpi = 300)
	if show:
		plt.show()
	else: 
		plt.close()


