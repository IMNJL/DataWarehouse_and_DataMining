# Slides for: Detecting Novel Associations in Large Data Sets — Reproduction

Slide 1 — Title
- Title: Detecting Novel Associations in Large Data Sets (Reshef et al., Science 2011)
- Subtitle: Reproduction & synthetic experiments (MIC-like vs R²)
- Presenter: [Your name]

Speaker notes:
 - One-sentence summary: Reshef et al. proposed the Maximal Information Coefficient (MIC) to detect a wide range of associations and to be more equitable across functional forms than simple linear measures.

Slide 2 — Goal & Plan
- Goal: Reproduce the paper's core intuition using synthetic relationships and our MIC-like implementation.
- Plan:
  - Generate several canonical relationships (linear, quadratic, sinusoid, exponential, cubic, step, circular, random)
  - Sweep additive noise and compute MIC-like and R² (linear-fit) scores
  - Visualize per-relationship score vs noise and an overall MIC vs R² scatter

Speaker notes:
 - Emphasize the goal is to demonstrate the intuition rather than an exact numeric replication of the paper's experiments.

Slide 3 — Methods: Synthetic data
- x ∈ [0,1], n = 500 samples, uniform sampling
- Relationships: linear, quadratic, sin(4πx), exponential, cubic, step, circular, random
- Noise: additive Gaussian, relative scale 0.0–1.0 (11 steps)

Speaker notes:
 - Noise added proportional to signal std to ensure comparable SNR across relationships.

Slide 4 — Metrics
- MIC-like: `minepy.MINE` if present; otherwise our deterministic fallback (R²-based) to keep experiments runnable.
- R² (linear): coefficient of determination from linear regression of y on x.

Speaker notes:
 - Note: for a faithful reproduction install `minepy` and re-run; instructions in the appendix.

Slide 5 — Overview of outputs
- Location: `DWH_1_Detecting_novel_associations_in_large_data_sets/outputs/`
- Files: `scores_vs_noise_<kind>.png` for each relationship, `mic_vs_r2_scatter.png`, and `experiment_results.csv`

Speaker notes:
 - We'll show per-relationship plots and the combined scatter to illustrate equitability.

Slide 6 — Linear (scores vs noise)
- Include figure: `outputs/scores_vs_noise_linear.png`
- Bullet: Both MIC-like and R² are high with low noise; both decrease as noise increases.

Speaker notes:
 - Linear relationships are well captured by R²; MIC is also high (expected).

Slide 7 — Quadratic (scores vs noise)
- Include figure: `outputs/scores_vs_noise_quadratic.png`
- Bullet: R² drops earlier than MIC-like, showing R²'s weakness for nonlinear shapes.

Speaker notes:
 - Emphasize that although the quadratic is a deterministic function, linear R² underestimates association strength.

Slide 8 — Sinusoid (scores vs noise)
- Include figure: `outputs/scores_vs_noise_sin.png`
- Bullet: MIC-like remains elevated relative to R² at moderate noise.

Speaker notes:
 - Sinusoidal relationships are classic examples where linear measures fail.

Slide 9 — Exponential (scores vs noise)
- Include figure: `outputs/scores_vs_noise_exponential.png`
- Bullet: Nonlinear trend detected better by MIC-like than linear R² at low-to-moderate noise.

Speaker notes:
 - Nonlinear monotonic functions can also lead to misleadingly low linear R².

Slide 10 — Cubic (scores vs noise)
- Include figure: `outputs/scores_vs_noise_cubic.png`
- Bullet: Shape-dependent differences between MIC-like and R².

Speaker notes:
 - Cubic is another deterministic but non-linear shape illustrating the point.

Slide 11 — Step (scores vs noise)
- Include figure: `outputs/scores_vs_noise_step.png`
- Bullet: Step function has low linear R² even with no noise; MIC-like captures the dependence.

Speaker notes:
 - Step and discontinuous relationships are difficult for linear regressions.

Slide 12 — Circular (scores vs noise)
- Include figure: `outputs/scores_vs_noise_circular.png`
- Bullet: Circular (non-functional) relationships cause R² to be near zero while MIC-like shows dependence.

Speaker notes:
 - Non-functional relationships are precisely the cases where MIC is intended to help.

Slide 13 — Random (scores vs noise)
- Include figure: `outputs/scores_vs_noise_random.png`
- Bullet: Both metrics near zero as expected; shows baseline behavior.

Speaker notes:
 - A sanity-check: random data should show no association.

Slide 14 — Combined MIC vs R² scatter
- Include figure: `outputs/mic_vs_r2_scatter.png`
- Bullet: Points above diagonal → MIC detects associations missed by R²; on-diagonal → agreement.

Speaker notes:
 - Explain legend mapping: each point is a (kind, noise) pair.

Slide 15 — Summary of results
- MIC-like is generally more equitable across function families than linear R².
- R² works well for linear relationships but underestimates many nonlinear associations.

Speaker notes:
 - Remind audience that numeric values depend on whether real `minepy` MIC or fallback was used.

Slide 16 — Data & outputs
- CSV: `outputs/experiment_results.csv` (per-kind, per-noise MIC and R²)
- Figures: all `outputs/scores_vs_noise_*.png` and `outputs/mic_vs_r2_scatter.png`

Speaker notes:
 - You can open the CSV to reproduce specific points on the scatter plot.

Slide 17 — Limitations
- We used a fallback MIC when `minepy` is not installed; values differ from the official MIC.
- Synthetic experiments are illustrative but not exhaustive; the paper uses real-world datasets and more metrics.

Speaker notes:
 - Be transparent: this is a demonstration and not a full numerical replication.

Slide 18 — Next steps
- Install `minepy` and re-run for official MIC values.
- Run experiments on the real datasets used in the paper (WHO stats, gene expression, MLB, microbiome).
- Optionally expand to mutual information estimators and compare with other MINE statistics.

Slide 19 — Appendix: reproducibility commands
- Create & activate venv; install deps; run experiments & presentation generator:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
python src/experiments.py
python src/make_presentation.py
```

Slide 20 — Contact
- Questions / feedback: [your-email@example.com]

Speaker notes:
 - Thank the audience; offer to share code and data.
