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

samples = loadMCSamples('./EXAMPLE_MCMC71',settings=analysissettings)
print("71  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC71_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC72',settings=analysissettings)
print("72  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC72_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC73',settings=analysissettings)
print("73  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC73_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC74',settings=analysissettings)
print("74  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC74_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC75',settings=analysissettings)
print("75  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC75_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC76',settings=analysissettings)
print("76  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC76_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC77',settings=analysissettings)
print("77  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC77_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC78',settings=analysissettings)
print("78  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC78_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC79',settings=analysissettings)
print("79  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC79_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC80',settings=analysissettings)
print("80  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC80_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC81',settings=analysissettings)
print("81  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC81_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC82',settings=analysissettings)
print("82  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC82_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC83',settings=analysissettings)
print("83  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC83_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC84',settings=analysissettings)
print("84  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC84_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC85',settings=analysissettings)
print("85  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC85_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC86',settings=analysissettings)
print("86  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC86_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC87',settings=analysissettings)
print("87  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC87_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC88',settings=analysissettings)
print("88  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC88_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC89',settings=analysissettings)
print("89  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC89_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC90',settings=analysissettings)
print("90  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC90_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC91',settings=analysissettings)
print("91  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC91_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC92',settings=analysissettings)
print("92  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC92_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC93',settings=analysissettings)
print("93  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC93_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC94',settings=analysissettings)
print("94  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC94_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC95',settings=analysissettings)
print("95  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC95_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC96',settings=analysissettings)
print("96  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC96_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC97',settings=analysissettings)
print("97  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC97_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC98',settings=analysissettings)
print("98  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC98_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC99',settings=analysissettings)
print("99  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC99_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC100',settings=analysissettings)
print("100  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC100_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC101',settings=analysissettings)
print("101  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC101_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC102',settings=analysissettings)
print("102  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC102_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC103',settings=analysissettings)
print("103  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC103_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC104',settings=analysissettings)
print("104  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC104_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC105',settings=analysissettings)
print("105  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC105_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC106',settings=analysissettings)
print("106  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC106_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC107',settings=analysissettings)
print("107  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC107_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC108',settings=analysissettings)
print("108  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC108_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC109',settings=analysissettings)
print("109  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC109_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC110',settings=analysissettings)
print("110  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC110_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC111',settings=analysissettings)
print("111  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC111_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC112',settings=analysissettings)
print("112  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC112_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC1000',settings=analysissettings)
print("1000 ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC1000_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC1001',settings=analysissettings)
print("1001  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC1001_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC1002',settings=analysissettings)
print("1002  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC1002_THIN')

samples = loadMCSamples('./EXAMPLE_MCMC1003',settings=analysissettings)
print("1003  ", np.sum(samples.weights)/num_points_thin)
samples.thin(factor = int(np.sum(samples.weights)/num_points_thin))
samples.saveAsText('EXAMPLE_MCMC1003_THIN')
