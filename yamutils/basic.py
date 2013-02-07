import itertools
import copy


def flatten(x):
    return list(itertools.chain(*x))


def uniqify(X):
    return [x for (i, x) in enumerate(X) if x not in X[:i]]


def pluck(listOfDicts, att):
    return [l[att] for l in listOfDicts]


def dict_inverse(x):
    y = {}
    for k in x.keys():
        for kk in x[k]:
            if kk in y:
                y[kk].append(k)
            else:
                y[kk] = [k]
    return y


def cname(cls):
    return cls.__class__.__module__ + '.' + cls.__class__.__name__
