import getdist.plots as gplot
from getdist import MCSamples
from getdist import loadMCSamples
import os
import matplotlib
import subprocess
import matplotlib.pyplot as plt
import numpy as np

num_points_thin = 5000

analysissettings={'smooth_scale_1D':0.35,'smooth_scale_2D':0.35,'ignore_rows': u'0.5',
'range_confidence' : u'0.005'}

samples = loadMCSamples('./EXAMPLE_MCMC0',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC0_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC1',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC1_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC2',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC2_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC3',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC3_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC4',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC4_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC5',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC5_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC6',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC6_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC7',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC7_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC8',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC8_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC9',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC9_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC10',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC10_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC11',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC11_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC12',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC12_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC13',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC13_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC14',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC14_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC15',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC15_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC16',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC16_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC17',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC17_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC18',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC18_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC19',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC19_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC20',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC20_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC21',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC21_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC22',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC22_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC23',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC23_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC24',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC24_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC25',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC25_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC26',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC26_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC27',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC27_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC28',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC28_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC29',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC29_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC30',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC30_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC31',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC31_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC32',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC32_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC33',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC34_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC35',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC35_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC36',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC36_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC37',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC37_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC38',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC38_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC39',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC39_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC40',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC40_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC41',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC41_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC42',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC42_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC43',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC43_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC44',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC44_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC45',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC45_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC46',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC46_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC47',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC47_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC48',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC48_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC49',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC49_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC50',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC50_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC51',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC51_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC52',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC52_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC53',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC53_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC54',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC54_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC55',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC55_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC56',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC56_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC57',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC57_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC58',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC58_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC59',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC59_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC60',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC60_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC61',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC61_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC62',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC62_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC63',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC63_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC64',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC64_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC65',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC65_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC66',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC66_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC67',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC67_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC68',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC68_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC69',settings=analysissettings)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC69_THIN')