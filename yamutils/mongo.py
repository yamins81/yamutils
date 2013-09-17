import copy
import datetime
import numpy as np

from bson.objectid import ObjectId


def combine_queries(a,b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    for k in b:
        if k == '$where' and k in a:
            a[k] = a[k].strip('; ') + ' && ' + b[k]
        elif k == '$or' and k in a:
            pass
        elif hasattr(b[k],'keys') and ('$in' in b[k] or '$nin' in b[k] or '$ne' in b[k]) and k in a:
            pass
        else:
            a[k] = b[k]
    return a
    

def get_most_recent(coll, q, skip=0, limit=0, kwargs=None):
    if kwargs is None:
        kwargs = {}
    C = coll.find(q, **kwargs).sort([("filename", 1), ("uploadDate", -1)]).skip(skip).limit(limit) 
    F = []
    for c in C:
        if len(F) == 0 or c['filename'] != F[-1]['filename']:
            F.append(c)
    return F


def SONify(arg, memo=None):
    if memo is None:
        memo = {}
    if id(arg) in memo:
        rval = memo[id(arg)]
    if isinstance(arg, ObjectId):
        rval = arg
    elif isinstance(arg, datetime.datetime):
        rval = arg
    elif isinstance(arg, np.floating):
        rval = float(arg)
    elif isinstance(arg, np.integer):
        rval = int(arg)
    elif isinstance(arg, (list, tuple)):
        rval = type(arg)([SONify(ai, memo) for ai in arg])
    elif isinstance(arg, dict):
        rval = dict([(SONify(k, memo), SONify(v, memo))
            for k, v in arg.items()])
    elif isinstance(arg, (basestring, float, int, type(None))):
        rval = arg
    elif isinstance(arg, np.ndarray):
        if arg.ndim == 0:
            rval = SONify(arg.sum())
        else:
            rval = map(SONify, arg) # N.B. memo None
    # -- put this after ndarray because ndarray not hashable
    elif arg in (True, False):
        rval = int(arg)
    else:
        raise TypeError('SONify', arg)
    memo[id(rval)] = rval
    return rval
