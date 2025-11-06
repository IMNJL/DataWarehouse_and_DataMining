import numpy as np
from src.mic_utils import compute_mic


def test_linear_mic_high():
    # Perfect linear relationship (no noise) should have a high score with either minepy or R² fallback
    x = np.linspace(0, 1, 200)
    y = 2.0 * x  # perfect linear
    score = compute_mic(x, y)
    # Accept a high threshold (0.9) to tolerate fallback behavior
    assert score >= 0.9, f"Expected high MIC-like score for perfect linear, got {score}"
