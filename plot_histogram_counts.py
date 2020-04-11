#!/bin/env python3

import os,sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.ticker import MaxNLocator

# plot histogram
def plot_histogram_counts(data):

	#find first non-zero entry in histogram
	idx = (data['Count'] != 0).idxmax(1)
	data = data[idx:]
	[xmin,xmax] = [(data['Length'].min() / 2),data['Length'].max() + 10]
	[ymin,ymax] = np.round([(data['Count'].min() / 2),data['Count'].max() + 10],-1)
	x_range = xmax - xmin
	y_range = ymax - ymin

	# set up figure
	fig = plt.figure(figsize=(10,10))
	p = plt.subplot()
	p.set_xlim([xmin, xmax])
	p.set_ylim([ymin, ymax])
	p.spines['right'].set_visible(False)
	p.spines['top'].set_visible(False)
	p.spines['left'].set_position(('axes', -0.05))
	p.spines['bottom'].set_position(('axes', -0.05))
	p.xaxis.set_ticks([np.int(xmin),np.int(xmax/2),np.int(xmax)])
	p.yaxis.set_ticks([ymin,ymax/2,ymax])
	p.yaxis.set_ticks_position('left')
	p.xaxis.set_ticks_position('bottom')
	p.set_yticklabels([np.int(xmin),np.int(xmax/2),np.int(xmax)])
	p.set_yticklabels([np.int(ymin),np.int(ymax/2),np.int(ymax)])
	plt.ylabel('Count')
	plt.xlabel('Length of Streamlines (mm)')
	color = mcolors.cnames['blue']
	plt.title("Histogram of streamline lengths")
	lines = data['Count'].plot.line()

	               
	#plt.show()
	hist_out = "tractlength-histrogram.png"
	plt.savefig(os.path.join('./',hist_out))

# load histogram data
data = pd.read_csv('hist.txt',sep=",",header=None)
data = data.drop(0)
data.columns = ['Length','Count']
data = data.astype(float)

# plot the histogram
plot_hist_counts(data)