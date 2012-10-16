#!/usr/bin/env python

import yamutils.stats as ystats
import scipy.stats as sstats
import numpy as np

def tests_pearsonr(rseed=0):
    rng = np.random.RandomState(seed=rseed)
    X = rng.uniform(size=(100, 50))
    Y = rng.uniform(size=(10, 50))
    
    yP = ystats.pearsonr(X.T, Y.T)[0]
    sP = np.array([[sstats.pearsonr(x, y)[0] for y in Y] for x in X])

    print yP.shape
    print sP.shape
    diff = np.abs(yP - sP)
    print diff
    print diff.min(), diff.max()

    assert diff.sum() < 1e-5


