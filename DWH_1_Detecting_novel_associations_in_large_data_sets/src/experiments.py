"""Run synthetic experiments comparing MIC-like score and R² across relationship types and noise levels.

Outputs saved to `../outputs/` as PNGs and a CSV summary.
"""
import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mic_utils import compute_mic
from sklearn.metrics import r2_score


def make_relationship(kind, x, noise_scale=0.0, rng=None):
    if rng is None:
        rng = np.random.RandomState(0)
    n = len(x)
    if kind == "linear":
        y = 2.0 * x
    elif kind == "quadratic":
        y = (4 * (x - 0.5) ** 2)
    elif kind == "sin":
        y = np.sin(4 * np.pi * x)
    elif kind == "exponential":
        y = np.exp(2 * x) - 1.0
    elif kind == "cubic":
        y = (x - 0.5) ** 3
    elif kind == "step":
        y = (x > 0.5).astype(float)
    elif kind == "circular":
        y = np.sqrt(np.clip(0.25 - (x - 0.5) ** 2, 0, None))
    else:
        y = rng.rand(n)

    if noise_scale > 0:
        y = y + rng.normal(scale=noise_scale * np.std(y) if np.std(y) > 0 else noise_scale, size=n)
    return y


def run_experiment(output_dir: str = "../outputs", n=500, noise_levels=None, kinds=None, seed=0):
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    if noise_levels is None:
        noise_levels = np.linspace(0.0, 1.0, 11)
    if kinds is None:
        kinds = ["linear", "quadratic", "sin", "exponential", "cubic", "step", "circular", "random"]

    rng = np.random.RandomState(seed)
    x = np.linspace(0, 1, n)

    records = []
    for kind in kinds:
        mic_vals = []
        r2_vals = []
        for noise in noise_levels:
            y = make_relationship(kind, x, noise_scale=noise, rng=rng)
            try:
                mic = compute_mic(x, y)
            except Exception as e:
                mic = float('nan')
            # R² from linear fit (as in paper comparison) - compute best-fit regression R²
            try:
                r2 = r2_score(y, np.poly1d(np.polyfit(x, y, deg=1))(x))
            except Exception:
                r = np.corrcoef(x, y)[0, 1]
                r2 = float(np.nan_to_num(r) ** 2)

            mic_vals.append(mic)
            r2_vals.append(max(0.0, min(1.0, float(np.nan_to_num(r2)))))
            records.append({"kind": kind, "noise": float(noise), "mic": float(mic), "r2": float(r2)})

        # Plot MIC & R² vs noise for this relationship type
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(noise_levels, mic_vals, marker='o', label='MIC-like')
        ax.plot(noise_levels, r2_vals, marker='s', label='R² (linear)')
        ax.set_xlabel('Noise scale (rel)')
        ax.set_ylabel('Score')
        ax.set_title(f"Scores vs noise — {kind}")
        ax.set_ylim(-0.05, 1.05)
        ax.grid(True)
        ax.legend()
        fig.tight_layout()
        fig_path = out / f"scores_vs_noise_{kind}.png"
        fig.savefig(fig_path)
        plt.close(fig)

    # Combined scatter MIC vs R² across all kinds and noise
    df = pd.DataFrame.from_records(records)
    fig, ax = plt.subplots(figsize=(6, 6))
    for kind in kinds:
        sub = df[df['kind'] == kind]
        ax.scatter(sub['r2'], sub['mic'], label=kind, alpha=0.7, s=30)
    ax.plot([0, 1], [0, 1], 'k--', alpha=0.5)
    ax.set_xlabel('R² (linear)')
    ax.set_ylabel('MIC-like')
    ax.set_title('MIC-like vs R² across relationships and noise')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_xlim(-0.01, 1.01)
    ax.set_ylim(-0.01, 1.01)
    fig.tight_layout()
    fig_path = out / "mic_vs_r2_scatter.png"
    fig.savefig(fig_path)
    plt.close(fig)

    # Save CSV
    csv_path = out / "experiment_results.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved figures to {out.resolve()} and CSV to {csv_path.resolve()}")


if __name__ == '__main__':
    run_experiment()
