import copy

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

