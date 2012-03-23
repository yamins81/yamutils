import numpy as np


def perminverse(s):
    '''
    Fast inverse of a (numpy) permutation.

    **Paramters**

            **s** :  sequence

                    Sequence of indices giving a permutation.

    **Returns**

            **inv** :  numpy array

                    Sequence of indices giving the inverse of permutation `s`.

    '''
    X = np.array(range(len(s)))
    X[s] = range(len(s))
    return X


def reorder_to(A, B):
    C = A.copy()
    C.sort()
    s = np.searchsorted(C, B)
    t = np.searchsorted(C, A)
    return perminverse(t)[s]


def uniqify(seq, idfun=None):
    """
    Relatively fast pure Python uniqification function that preservs ordering.

    **Parameters**

            **seq** :  sequence

                    Sequence object to uniqify.

            **idfun** :  function, optional

                    Optional collapse function to identify items as the same.

    **Returns**

            **result** :  list

                    Python list with first occurence of each item in `seq`, in 
                    order.

    """
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

    
def equalspairs(X, Y):
    """
    Indices of elements in a sorted numpy array equal to those in another.

    Given numpy array `X` and sorted numpy array `Y`, determine the indices in 
    Y equal to indices in X.

    Returns `[A,B]` where `A` and `B` are numpy arrays of indices in `X` such 
    that::

            Y[A[i]:B[i]] = Y[Y == X[i]]`

    `A[i] = B[i] = 0` if `X[i]` is not in `Y`.

    **Parameters**

            **X** :  numpy array

                    Numpy array to compare to the sorted numpy array `Y`.

            **Y** :  numpy array

                    Sorted numpy array.  Determine the indices of elements of 
                    `Y` equal to those in numpy array `X`.

    **Returns**

            **A** :  numpy array

                    List of indices in `Y`, `len(A) = len(Y)`.

            **B** :  numpy array

                    List of indices in `Y`, `len(B) = len(Y)`.

    **See Also:**

            :func:`tabular.fast.recarrayequalspairs`

    """
    T = Y.copy()
    R = (T[1:] != T[:-1]).nonzero()[0]
    R = np.append(R,np.array([len(T)-1]))
    M = R[R.searchsorted(range(len(T)))]
    D = T.searchsorted(X)
    T = np.append(T,np.array([0]))
    M = np.append(M,np.array([0]))
    A = (T[D] == X) * D
    B = (T[D] == X) * (M[D] + 1)
    return [A,B]


def isin(X,Y):
    """
    Indices of elements in a numpy array that appear in another.

    Fast routine for determining indices of elements in numpy array `X` that 
    appear in numpy array `Y`, returning a boolean array `Z` such that::

            Z[i] = X[i] in Y

    **Parameters**

            **X** :  numpy array

                    Numpy array to comapare to numpy array `Y`.  For each 
                    element of `X`, ask if it is in `Y`.

            **Y** :  numpy array

                    Numpy array to which numpy array `X` is compared.  For each 
                    element of `X`, ask if it is in `Y`.

    **Returns**

            **b** :  numpy array (bool)

                    Boolean numpy array, `len(b) = len(X)`.

    **See Also:**

            :func:`tabular.fast.recarrayisin`, 
            :func:`tabular.fast.arraydifference`

    """
    if len(Y) > 0:
        T = Y.copy()
        T.sort()
        D = T.searchsorted(X)
        T = np.append(T,np.array([0]))
        W = (T[D] == X)
        if isinstance(W,bool):
            return np.zeros((len(X),),bool)
        else:
            return (T[D] == X)
    else:
        return np.zeros((len(X),),bool)
