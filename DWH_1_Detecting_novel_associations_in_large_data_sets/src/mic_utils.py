"""
Utility functions to compute an MIC-like score between two 1D arrays.

Behavior:
- If `minepy.MINE` is importable, use it to compute MIC.
- Otherwise, fall back to a fast R²-based approximation using scikit-learn's r2_score.

The fallback is intentionally simple and deterministic; it ensures the demo and tests run
without needing to compile C extensions.
"""
from typing import Sequence
import numpy as np

try:
    from minepy import MINE  # type: ignore
except Exception:
    MINE = None

try:
    from sklearn.metrics import r2_score
except Exception:
    r2_score = None


def compute_mic(x: Sequence[float], y: Sequence[float], **minepy_kwargs) -> float:
    """Compute an MIC-like score between x and y.

    Returns a float in [0, 1].

    - If `minepy` is available, returns the official MIC from MINE.
    - Otherwise, returns max(0, min(1, R²)) as a fallback approximation.

    Args:
        x, y: 1-D numeric sequences of equal length.
        minepy_kwargs: forwarded to `MINE(**kwargs)` when using minepy.
    """
    x_arr = np.asarray(x).ravel()
    y_arr = np.asarray(y).ravel()
    if x_arr.shape[0] != y_arr.shape[0]:
        raise ValueError("x and y must have the same length")

    if MINE is not None:
        mine = MINE(**minepy_kwargs)
        # minepy expects finite numeric arrays
        mine.compute_score(x_arr, y_arr)
        mic_val = float(mine.mic())
        # ensure numeric range
        return max(0.0, min(1.0, mic_val))

    # Fallback: use R² if available
    if r2_score is None:
        raise RuntimeError("Neither minepy nor scikit-learn are available. Install scikit-learn or minepy.")

    try:
        r2 = r2_score(y_arr, np.poly1d(np.polyfit(x_arr, y_arr, deg=1))(x_arr))
    except Exception:
        # polyfit can fail for degenerate inputs; fall back to Pearson r²
        r = np.corrcoef(x_arr, y_arr)[0, 1]
        r2 = float(np.nan_to_num(r) ** 2)

    return float(max(0.0, min(1.0, r2)))


def compute_pairwise_mic(df, columns=None):
    """Compute pairwise MIC-like matrix for columns in a DataFrame (or 2D array-like).

    Returns a pandas DataFrame of pairwise scores when given a DataFrame; otherwise returns
    a square numpy array.
    """
    import pandas as pd

    if columns is None and hasattr(df, "columns"):
        columns = list(df.columns)

    data = pd.DataFrame(df)[columns]
    n = len(columns)
    mat = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i, n):
            s = compute_mic(data.iloc[:, i].values, data.iloc[:, j].values)
            mat[i, j] = s
            mat[j, i] = s

    return pd.DataFrame(mat, index=columns, columns=columns)
