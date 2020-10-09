# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

# Demo python notebook for sklearn elm and random_hidden_layer modules
#
# Author: David C. Lambert [dcl -at- panix -dot- com]
# Copyright(c) 2013
# License: Simple BSD

# <codecell>

from time import time
from sklearn.cluster import k_means

from elm import ELMClassifier, ELMRegressor, GenELMClassifier, GenELMRegressor
from random_layer import RandomLayer, MLPRandomLayer, RBFRandomLayer, GRBFRandomLayer

# <codecell>

def make_toy():
    x = np.arange(0.25,20,0.1)
    y = x*np.cos(x)+0.5*sqrt(x)*np.random.randn(x.shape[0])
    x = x.reshape(-1,1)
    y = y.reshape(-1,1)
    return x, y

# <codecell>

def res_dist(x, y, e, n_runs=100, random_state=None):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=random_state)

    test_res = []
    train_res = []
    start_time = time()

    for i in xrange(n_runs):
        e.fit(x_train, y_train)
        train_res.append(e.score(x_train, y_train))
        test_res.append(e.score(x_test, y_test))
        if (i%(n_runs/10) == 0): print "%d"%i,

    print "\nTime: %.3f secs" % (time() - start_time)

    print "Test Min: %.3f Mean: %.3f Max: %.3f SD: %.3f" % (min(test_res), mean(test_res), max(test_res), std(test_res))
    print "Train Min: %.3f Mean: %.3f Max: %.3f SD: %.3f" % (min(train_res), mean(train_res), max(train_res), std(train_res))
    print
    return (train_res, test_res)

# <codecell>

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris, load_digits, load_diabetes, make_regression

stdsc = StandardScaler()

iris = load_iris()
irx, iry = stdsc.fit_transform(iris.data), iris.target
irx_train, irx_test, iry_train, iry_test = train_test_split(irx, iry, test_size=0.2)

digits = load_digits()
dgx, dgy = stdsc.fit_transform(digits.data/16.0), digits.target
dgx_train, dgx_test, dgy_train, dgy_test = train_test_split(dgx, dgy, test_size=0.2)

diabetes = load_diabetes()
dbx, dby = stdsc.fit_transform(diabetes.data), diabetes.target
dbx_train, dbx_test, dby_train, dby_test = train_test_split(dbx, dby, test_size=0.2)

mrx, mry = make_regression(n_samples=2000, n_targets=4)
mrx_train, mrx_test, mry_train, mry_test = train_test_split(mrx, mry, test_size=0.2)

xtoy, ytoy = make_toy()
xtoy, ytoy = stdsc.fit_transform(xtoy), stdsc.fit_transform(ytoy)
xtoy_train, xtoy_test, ytoy_train, ytoy_test = train_test_split(xtoy, ytoy, test_size=0.2)
plot(xtoy, ytoy)

# <codecell>

# RBFRandomLayer tests
for af in RandomLayer.activation_func_names():
    print af,
    elmc = ELMClassifier(activation_func=af)
    tr,ts = res_dist(irx, iry, elmc, n_runs=200, random_state=0)

# <codecell>

elmc.classes_

# <codecell>

for af in RandomLayer.activation_func_names():
    print af
    elmc = ELMClassifier(activation_func=af, random_state=0)
    tr,ts = res_dist(dgx, dgy, elmc, n_runs=100, random_state=0)

# <codecell>

elmc = ELMClassifier(n_hidden=500, activation_func='multiquadric')
tr,ts = res_dist(dgx, dgy, elmc, n_runs=100, random_state=0)
scatter(tr, ts, alpha=0.1, marker='D', c='r')

# <codecell>

elmr = ELMRegressor(random_state=0, activation_func='gaussian', alpha=0.0)
elmr.fit(xtoy_train, ytoy_train)
print elmr.score(xtoy_train, ytoy_train), elmr.score(xtoy_test, ytoy_test)
plot(xtoy, ytoy, xtoy, elmr.predict(xtoy))

# <codecell>

from sklearn import pipeline
from sklearn.linear_model import LinearRegression
elmr = pipeline.Pipeline([('rhl', RandomLayer(random_state=0, activation_func='multiquadric')),
                          ('lr', LinearRegression(fit_intercept=False))])
elmr.fit(xtoy_train, ytoy_train)
print elmr.score(xtoy_train, ytoy_train), elmr.score(xtoy_test, ytoy_test)
plot(xtoy, ytoy, xtoy, elmr.predict(xtoy))

# <codecell>

rhl = RandomLayer(n_hidden=200, alpha=1.0)
elmr = GenELMRegressor(hidden_layer=rhl)
tr, ts = res_dist(mrx, mry, elmr, n_runs=200, random_state=0)
scatter(tr, ts, alpha=0.1, marker='D', c='r')

# <codecell>

rhl = RBFRandomLayer(n_hidden=15, rbf_width=0.8)
elmr = GenELMRegressor(hidden_layer=rhl)
elmr.fit(xtoy_train, ytoy_train)
print elmr.score(xtoy_train, ytoy_train), elmr.score(xtoy_test, ytoy_test)
plot(xtoy, ytoy, xtoy, elmr.predict(xtoy))

# <codecell>

nh = 15
(ctrs, _, _) = k_means(xtoy_train, nh)
unit_rs = np.ones(nh)

#rhl = RBFRandomLayer(n_hidden=nh, activation_func='inv_multiquadric')
#rhl = RBFRandomLayer(n_hidden=nh, centers=ctrs, radii=unit_rs)
rhl = GRBFRandomLayer(n_hidden=nh, grbf_lambda=.0001, centers=ctrs)
elmr = GenELMRegressor(hidden_layer=rhl)
elmr.fit(xtoy_train, ytoy_train)
print elmr.score(xtoy_train, ytoy_train), elmr.score(xtoy_test, ytoy_test)
plot(xtoy, ytoy, xtoy, elmr.predict(xtoy))

# <codecell>

rbf_rhl = RBFRandomLayer(n_hidden=100, random_state=0, rbf_width=0.01)
elmc_rbf = GenELMClassifier(hidden_layer=rbf_rhl)
elmc_rbf.fit(dgx_train, dgy_train)
print elmc_rbf.score(dgx_train, dgy_train), elmc_rbf.score(dgx_test, dgy_test)

def powtanh_xfer(activations, power=1.0):
    return pow(np.tanh(activations), power)

tanh_rhl = MLPRandomLayer(n_hidden=100, activation_func=powtanh_xfer, activation_args={'power':3.0})
elmc_tanh = GenELMClassifier(hidden_layer=tanh_rhl)
elmc_tanh.fit(dgx_train, dgy_train)
print elmc_tanh.score(dgx_train, dgy_train), elmc_tanh.score(dgx_test, dgy_test)

# <codecell>

rbf_rhl = RBFRandomLayer(n_hidden=100, rbf_width=0.01)
tr, ts = res_dist(dgx, dgy, GenELMClassifier(hidden_layer=rbf_rhl), n_runs=100, random_state=0)

# <codecell>

hist(ts), hist(tr)
print

# <codecell>

from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
tr, ts = res_dist(dbx, dby, RandomForestRegressor(n_estimators=15), n_runs=100, random_state=0)
hist(tr), hist(ts)
print

rhl = RBFRandomLayer(n_hidden=15, rbf_width=0.1)
tr,ts = res_dist(dbx, dby, GenELMRegressor(rhl), n_runs=100, random_state=0)
hist(tr), hist(ts)
print

# <codecell>

elmc = ELMClassifier(n_hidden=1000, activation_func='gaussian', alpha=0.0, random_state=0)
elmc.fit(dgx_train, dgy_train)
print elmc.score(dgx_train, dgy_train), elmc.score(dgx_test, dgy_test)

# <codecell>

elmc = ELMClassifier(n_hidden=500, activation_func='hardlim', alpha=1.0, random_state=0)
elmc.fit(dgx_train, dgy_train)
print elmc.score(dgx_train, dgy_train), elmc.score(dgx_test, dgy_test)

# <codecell>

elmr = ELMRegressor(random_state=0)
elmr.fit(xtoy_train, ytoy_train)
print elmr.score(xtoy_train, ytoy_train), elmr.score(xtoy_test, ytoy_test)
plot(xtoy, ytoy, xtoy, elmr.predict(xtoy))

# <codecell>

elmr = ELMRegressor(activation_func='inv_tribas', random_state=0)
elmr.fit(xtoy_train, ytoy_train)
print elmr.score(xtoy_train, ytoy_train), elmr.score(xtoy_test, ytoy_test)
plot(xtoy, ytoy, xtoy, elmr.predict(xtoy))
