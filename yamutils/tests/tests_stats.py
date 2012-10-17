#!/usr/bin/env python

import yamutils.stats as ystats
import scipy.stats as sstats
import numpy as np

def test_pearsonr(rseed=0):
    rng = np.random.RandomState(seed=rseed)
    X = rng.uniform(size=(200, 100))
    Y = rng.uniform(size=(500, 100))
    
    yP = ystats.pearsonr(X.T, Y.T)[0]
    sP = np.array([[sstats.pearsonr(x, y)[0] for y in Y] for x in X])

    print yP.shape
    print sP.shape
    diff = np.abs(yP - sP)

    assert diff.sum() < 1e-5


def test_pearsonr2(rseed=0):
    rng = np.random.RandomState(seed=rseed)
    X = 10 * rng.uniform(size=(200, 100))
    Y = rng.uniform(size=(500, 100)) - 0.5
    
    yP = ystats.pearsonr(X.T, Y.T)[0]
    sP = np.array([[sstats.pearsonr(x, y)[0] for y in Y] for x in X])

    print yP.shape
    print sP.shape
    diff = np.abs(yP - sP)
    assert diff.sum() < 1e-5
    
    
def test_pearsonr3(rseed=0):
    rng = np.random.RandomState(seed=rseed)
    X = 10 * np.ones((200, 100)) + .001 * rng.uniform(size=(200, 100))
    Y = .002 * rng.uniform(size=(500, 100))
    
    yP = ystats.pearsonr(X.T, Y.T)[0]
    sP = np.array([[sstats.pearsonr(x, y)[0] for y in Y] for x in X])

    print yP.shape
    print sP.shape
    diff = np.abs(yP - sP)
    assert diff.sum() < 1e-5