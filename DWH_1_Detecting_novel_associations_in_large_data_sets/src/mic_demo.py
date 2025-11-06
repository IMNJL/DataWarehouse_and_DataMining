"""Small demo that generates toy data and computes MIC-like scores.

Run with:
    python3 src/mic_demo.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mic_utils import compute_mic, compute_pairwise_mic


def make_toy_data(n=300, noise=0.05, seed=0):
    rng = np.random.RandomState(seed)
    x = np.linspace(0, 1, n)
    y_linear = 3.0 * x + rng.normal(scale=noise, size=n)
    y_sin = np.sin(4 * np.pi * x) + rng.normal(scale=noise * 0.5, size=n)
    y_random = rng.rand(n)
    return pd.DataFrame({"x": x, "linear": y_linear, "sin": y_sin, "rnd": y_random})


def main():
    df = make_toy_data()
    print("First rows of the dataset:\n", df.head())

    print("\nPairwise MIC-like scores: (rows=cols)")
    mic_df = compute_pairwise_mic(df)
    print(mic_df.round(3))

    # Print MIC between x and each target column
    print("\nMIC-like between 'x' and each variable:")
    for c in df.columns:
        if c == "x":
            continue
        s = compute_mic(df["x"].values, df[c].values)
        print(f"x vs {c}: {s:.3f}")

    # Quick scatter plot for visual check
    pairs = [("x", "linear"), ("x", "sin"), ("x", "rnd")]
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    for ax, (a, b) in zip(axs, pairs):
        ax.scatter(df[a], df[b], s=8, alpha=0.6)
        ax.set_xlabel(a)
        ax.set_ylabel(b)
        ax.grid(True)
    fig.suptitle("Toy relationships (MIC-like demo)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
