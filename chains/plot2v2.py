import getdist.plots as gplot
from getdist import MCSamples
from getdist import loadMCSamples
import os
import matplotlib
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# GENERAL PLOT OPTIONS
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
matplotlib.rcParams['xtick.bottom'] = True
matplotlib.rcParams['xtick.top'] = False
matplotlib.rcParams['ytick.right'] = False
matplotlib.rcParams['axes.edgecolor'] = 'black'
matplotlib.rcParams['axes.linewidth'] = '1.0'
matplotlib.rcParams['axes.labelsize'] = 'medium'
matplotlib.rcParams['axes.grid'] = True
matplotlib.rcParams['grid.linewidth'] = '0.0'
matplotlib.rcParams['grid.alpha'] = '0.18'
matplotlib.rcParams['grid.color'] = 'lightgray'
matplotlib.rcParams['legend.labelspacing'] = 0.77
matplotlib.rcParams['savefig.bbox'] = 'tight'
matplotlib.rcParams['savefig.format'] = 'pdf'

# ADDING NEFF AS DERIVED PARAMETER
parameter = [u's8omegamp5',u'omegam',u'omegam_growth',u'DES_A1_1',u'DES_A1_2',u'DES_A2_1',u'DES_A2_2']
chaindir=r'.'

analysissettings={'smooth_scale_1D':0.45,'smooth_scale_2D':0.45,'ignore_rows': u'0.3',
'range_confidence' : u'0.025'}

#GET DIST PLOT SETUP
g=gplot.getSubplotPlotter(chain_dir=chaindir,
analysis_settings=analysissettings,width_inch=10.0)
g.settings.lw_contour = 1.2
g.settings.legend_rect_border = False
g.settings.figure_legend_frame = False
g.settings.axes_fontsize = 13.5
g.settings.legend_fontsize = 15.5
g.settings.alpha_filled_add = 0.7
g.settings.lab_fontsize=15
g.legend_labels=False

param_3d = None
g.triangle_plot(['EXAMPLE_MCMC4', 'EXAMPLE_MCMC3'],parameter,
plot_3d_with_param=param_3d,line_args=[
{'lw': 1.0,'ls': 'solid', 'color':'royalblue'},
{'lw': 1.6,'ls': 'solid', 'color':'firebrick'},
{'lw': 1.9,'ls': 'dashed', 'color':'black'}],
contour_colors=['royalblue','firebrick','black'],
filled=True,shaded=False,
legend_labels=['SO + SN + DES-Y3', 'SO + SN + DES-Y1'],legend_loc=(0.5,0.825),
imax_shaded=0)
g.export()