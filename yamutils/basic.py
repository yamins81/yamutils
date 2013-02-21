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


def recursive_file_list(x):
    X = os.listdir(x)
    files = filter(lambda _x: os.path.isfile(os.path.join(x, _x)), X)
    dirs = filter(lambda _x: os.path.isdir(os.path.join(x, _x)), X)
    D = [recursive_file_list(os.path.join(x, d)) for d in dirs]
    D = list(itertools.chain(*D))
    return D + [os.path.join(x, f) for f in files]