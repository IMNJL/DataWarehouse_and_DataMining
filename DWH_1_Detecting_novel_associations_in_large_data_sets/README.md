# Detecting Novel Associations in Large Data Sets (Reshef et al. 2011)

This small project contains code to compute the Maximal Information Coefficient (MIC) for pairs of variables, a demo script with toy datasets, and a pytest test.

Notes:
- The original MIC algorithm is implemented in the `minepy` package (optional). This project will use `minepy` if installed.
- If `minepy` is not available, the package falls back to a fast approximation based on the coefficient of determination (R²). The fallback is intentionally simple to avoid heavy build dependencies.

Files added:
- `requirements.txt` – minimal dependencies to run the demo and tests
- `src/mic_utils.py` – compute_mic wrapper (minepy optional)
- `src/mic_demo.py` – demo script generating toy datasets and printing MICs
- `tests/test_mic.py` – pytest test for a near-perfect linear relationship

Quick start (macOS / zsh):

1) Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies:

```bash
python -m pip install -U pip
python -m pip install -r requirements.txt
```

3) Run the demo:

```bash
python src/mic_demo.py
```

4) Run tests:

```bash
pytest -q
```

Optional: to get the full MIC implementation, install `minepy` in your environment:

```bash
python -m pip install minepy
```

License: Educational copy for the Reshef (2011) paper demonstration.
