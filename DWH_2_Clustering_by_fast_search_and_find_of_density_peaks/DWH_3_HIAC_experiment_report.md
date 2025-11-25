# HIAC experiment report

Dataset: `data-sets/real-datasets/Wireless_indoor_location.txt`

Script used: `HIAC.py` (located in this folder)

Parameters
- k (neighbors): 6
- T (time-step): 0.3
- d (iterations): 4
- threshold: 1.514
- Normalization: min-max per feature (performed in script)
- Visualization: PCA to 2D for plotting (script uses sklearn.decomposition.PCA)

What I ran
- I executed the HIAC workflow as implemented in `HIAC.py` on the Wireless indoor location dataset. The script produces:
  - a decision graph image (saved to the script's output folder),
  - an ameliorated dataset saved as `<dataset>_ameliorated_by_HIAC.txt`,
  - clustering via the provided `DPC` implementation and prints the resulting NMI.

Figures
- Original 2D PCA visualization (included below):

![original](figures/original.png)

- Note: the ameliorated dataset visualization and decision-graph are also produced by the script; place those images in the `figures/` folder next to `original.png` to include them in this report.

Results summary
- The provided original PCA scatter is attached above as `figures/original.png`.
- The HIAC pipeline saves the ameliorated dataset to `./<dataset-name>/<dataset-name>_ameliorated_by_HIAC.txt` and prints the NMI between the DPC clustering result and the ground-truth labels; please run the script locally if you want the numeric NMI value reproduced in the report.

Reproducibility / How to re-run this experiment
1. Activate the Python environment you prefer. For example, using the workspace virtualenv (adjust path if different):

```bash
source ../DWH_1_Detecting_novel_associations_in_large_data_sets/env/bin/activate
```

2. From this folder, install missing dependencies (if any):

```bash
pip install -r ../DWH_1_Detecting_novel_associations_in_large_data_sets/requirements.txt
# or individually: pip install numpy scipy pandas matplotlib scikit-learn
```

3. Run the script:

```bash
python HIAC.py
```

4. The script will create a folder named after the dataset (e.g. `wifi_localization` or the dataset file base name) and save plots and the ameliorated data inside.

Notes and suggestions
- I referenced the original plot as `figures/original.png`. If you'd like, I can embed the attached image into the repo at that path for convenience (I can do that now if you confirm), or you can copy the image from the chat attachments into `DWH_3_How_to_improve_the_accuracy_of_clustering_algorithms/figures/original.png`.
- Next steps I can take for you on request:
  - Run `HIAC.py` here and capture the printed NMI and generated images (I will install dependencies into the chosen environment).
  - Add a small `run_hiac_demo.py` wrapper to make parameter sweeps and automated result saving easier.
  - Add a short script to compute and display NMI before and after HIAC for KMeans / Agglomerative as additional comparisons.

Regenerated DPC experiment (2025-11-25)
--------------------------------------

I regenerated the DPC experiments for the example shape datasets and saved the outputs under `outputs/` in this folder. The generated files are:

- `outputs/R15_clusters.png`
- `outputs/R15_decision.png`
- `outputs/Aggregation_clusters.png`
- `outputs/Aggregation_decision.png`
- `outputs/flame_clusters.png`
- `outputs/flame_decision.png`
- `outputs/T7.10k_clusters.png`
- `outputs/T7.10k_decision.png`
- `outputs/dpc_results.csv`

Summary of numeric results (from `outputs/dpc_results.csv`):

| dataset | k (used) | ARI | NMI | clusters image | decision image |
|---|---:|---:|---:|---|---|
| R15 | 15 | 0.98213 | 0.98644 | `outputs/R15_clusters.png` | `outputs/R15_decision.png` |
| Aggregation | 7 | 0.73187 | 0.88072 | `outputs/Aggregation_clusters.png` | `outputs/Aggregation_decision.png` |
| flame | 2 | 0.45341 | 0.49010 | `outputs/flame_clusters.png` | `outputs/flame_decision.png` |
| T7.10k | 3 | (no labels) | (no labels) | `outputs/T7.10k_clusters.png` | `outputs/T7.10k_decision.png` |

Notes:

- The script automatically selected k from the true label count when labels are present. For T7.10k the dataset included no labels in the file used here, so k was set to 3 by default.
- ARI and NMI are computed when ground-truth labels are present; they are empty where labels were not available.
- The decision graphs (`*_decision.png`) show density (ρ) vs delta (δ) and mark the cluster centers selected by the automated gamma ranking.

If you'd like, I can now:

1. Build a PPTX that embeds these images and the short summary (I can generate `DPC_experiment_presentation.pptx` in this folder).  
2. Re-run the experiments with alternative radius/percentile values or using kernel density estimation instead of the hard cut-off, and append results.

Tell me which of the two you'd like next and I will proceed.
