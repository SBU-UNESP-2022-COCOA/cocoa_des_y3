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
parameter = [u'omegam',u'sigma8',u'ns',u'H0',u'SS8',u'w']
chaindir=r'.'

analysissettings={'smooth_scale_1D':0.35,'smooth_scale_2D':0.35,'ignore_rows': u'0.35',
'range_confidence' : u'0.005'}

analysissettings2={'smooth_scale_1D':0.35,'smooth_scale_2D':0.35,'ignore_rows': u'0.0',
'range_confidence' : u'0.005'}

root_chains = ('EXAMPLE_MCMC24','EXAMPLE_MCMC25','EXAMPLE_MCMC18','EXAMPLE_MCMC19')

# --------------------------------------------------------------------------------
samples=loadMCSamples('./' + root_chains[0],settings=analysissettings)
p = samples.getParams()
samples.addDerived(p.omegam*p.H0/100.,name='gamma',label='{\\Omega_m h}')
samples.addDerived(p.s8omegamp5/0.5477225575,name='SS8',label='{S_8}')
samples.saveAsText('.VM_P0v4_TMP1')
# --------------------------------------------------------------------------------
samples=loadMCSamples('./' + root_chains[1],settings=analysissettings)
p = samples.getParams()
samples.addDerived(p.omegam*p.H0/100.,name='gamma',label='{\Gamma}')
samples.addDerived(p.s8omegamp5/0.5477225575,name='SS8',label='{S_8}')
samples.saveAsText('.VM_P0v4_TMP2')
# --------------------------------------------------------------------------------
samples=loadMCSamples('./' + root_chains[2],settings=analysissettings)
p = samples.getParams()
samples.addDerived(p.omegam*p.H0/100.,name='gamma',label='{\Gamma}')
samples.addDerived(p.s8omegamp5/0.5477225575,name='SS8',label='{S_8}')
samples.saveAsText('.VM_P0v4_TMP3')
# --------------------------------------------------------------------------------
samples=loadMCSamples('./' + root_chains[3],settings=analysissettings)
p = samples.getParams()
samples.addDerived(p.omegam*p.H0/100.,name='gamma',label='{\Gamma}')
samples.addDerived(p.s8omegamp5/0.5477225575,name='SS8',label='{S_8}')
samples.saveAsText('.VM_P0v4_TMP4')

#GET DIST PLOT SETUP
g=gplot.getSubplotPlotter(chain_dir=chaindir,
analysis_settings=analysissettings2,width_inch=9.0)
g.settings.axis_tick_x_rotation=65
g.settings.lw_contour = 1.2
g.settings.legend_rect_border = False
g.settings.figure_legend_frame = False
g.settings.axes_fontsize = 14.0
g.settings.legend_fontsize = 16.75
g.settings.alpha_filled_add = 0.7
g.settings.lab_fontsize=20
g.legend_labels=False

param_3d = None
g.triangle_plot(['.VM_P0v4_TMP1','.VM_P0v4_TMP2','.VM_P0v4_TMP3','.VM_P0v4_TMP4'],parameter,
plot_3d_with_param=param_3d,line_args=[
{'lw': 1.2,'ls': 'solid', 'color':'cornflowerblue'},
{'lw': 1.2,'ls': 'solid', 'color': 'darkgoldenrod'},
{'lw': 1.5,'ls': '-.', 'color': 'firebrick'},
{'lw': 2.0,'ls': '--', 'color': 'indigo'},
],
contour_colors=['cornflowerblue','darkgoldenrod','firebrick','indigo'],
contour_ls=['solid','solid','-.','--'], 
contour_lws=[1.0,1.0,2.0,2.0],
filled=[True,True,False,False],
shaded=False,
legend_labels=[
'DES-Y1 (3x2pt)',
'DES-Y3 (3x2pt)',
'SN Pantheon + BAO + BBN',
'Planck low-$\\ell_{\\mathrm{EE}}$ + Planck high-$\\ell_{\\mathrm{TTTEEE}}$ (33 < $\\ell$ < 396)',
],
legend_loc=(0.42,0.825))

# Vertical Line - Omegam
for ax in g.subplots[:,0]:
  if ax is not None:
    ax.axvline(0.3166,color='gray', ls='--',alpha=0.3)
# Vertical Line - ns
for ax in g.subplots[:,1]:
  if ax is not None:
    ax.axvline(0.81337, color='gray', ls='--',alpha=0.3)
# Vertical Line - H0
for ax in g.subplots[:,2]:
  if ax is not None:
    ax.axvline(0.9649, color='gray', ls='--',alpha=0.3)
for ax in g.subplots[:,3]:
  if ax is not None:
    ax.axvline(67.32, color='gray', ls='--',alpha=0.3)
for ax in g.subplots[:,4]:
  if ax is not None:
    ax.axvline(0.83557, color='gray', ls='--',alpha=0.3)
for ax in g.subplots[:,5]:
  if ax is not None:
    ax.axvline(-1, color='gray', ls='--',alpha=0.3)

# Horizontal - ns
for ax in g.subplots[1,0:1]:
  if ax is not None:
    ax.axhline(0.81337, color='gray', ls='--',alpha=0.3)
for ax in g.subplots[2,0:2]:
  if ax is not None:
    ax.axhline(0.9649, color='gray', ls='--',alpha=0.3)
for ax in g.subplots[3,0:3]:
  if ax is not None:
    ax.axhline(67.32, color='gray', ls='--',alpha=0.3)
for ax in g.subplots[4,0:4]:
  if ax is not None:
    ax.axhline(0.83557, color='gray', ls='--',alpha=0.3)
for ax in g.subplots[5,0:5]:
  if ax is not None:
    ax.axhline(-1, color='gray', ls='--',alpha=0.3)

g.export()