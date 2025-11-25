# DPC experiment (reproduction of Rodriguez & Laio, 2014)

This folder includes a small experiment harness to run the DPC algorithm on several shape datasets and to generate a PowerPoint summarizing results.

Files added:
- `run_dpc_experiments.py` — script that runs DPC on example datasets and saves images and `dpc_results.csv` in `outputs/`.
- `create_pptx.py` — builds a PowerPoint from `slide_contents.json` and images under `outputs/`.
- `slide_contents.json` — slide text and image references.
- `requirements_experiment.txt` — python package list.

Quick steps (macOS / zsh):

1. Create-and-activate a virtualenv (optional):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install requirements:

```bash
pip install -r requirements_experiment.txt
```

3. Run experiments:

```bash
python run_dpc_experiments.py
```

4. Build PPTX:

```bash
python create_pptx.py --images-dir outputs --slide-json slide_contents.json --out DPC_experiment_presentation.pptx
```

Outputs will be under `outputs/`.

Notes:
- The included `DPC.py` implements the cut-off variant of the algorithm (uses 2% percentile as radius like in the original code here). The script uses the true label counts to automate k selection for the demo datasets.
- For a human-like reproduction of the paper's decision-graph workflow, inspect the decision graph PNGs and select centers interactively; the script picks top-k by gamma automatically to allow batch runs.
