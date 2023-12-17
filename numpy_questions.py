import numpy as np


def max_index(X):
    """
    Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    (i, j) : tuple(int)
        The row and column index of the maximum.

    Raises
    ------
    ValueError
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise ValueError("Input must be a 2D numpy array")

    i, j = np.unravel_index(np.argmax(X), X.shape)
    return i, j


def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    See:
    https://en.wikipedia.org/wiki/Wallis_product

    Parameters
    ----------
    n_terms : int
        Number of steps in the Wallis product. Note that `n_terms=0` will
        consider the product to be `1`.

    Returns
    -------
    pi : float
        The approximation of order `n_terms` of pi using the Wallis product.
    """
    # XXX : The n_terms is an int that corresponds to the number of
    # terms in the product. For example 10000.
    if n_terms == 0:
        return 2.0

    product = 1.0
    for i in range(1, n_terms + 1):
        term = (2.0 * i) / (2.0 * i - 1) * (2.0 * i) / (2.0 * i + 1)
        product *= term

    return product * 2
