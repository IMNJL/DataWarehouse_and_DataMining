#!/usr/bin/env python3
"""Run DPC experiments on included shape datasets and save figures/results.

Creates per-dataset plots: data colored by found cluster, decision graph (density vs delta), and saves a CSV with ARI/NMI when labels exist.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

from DPC import DPC

ROOT = os.path.dirname(__file__)
DATA_DIR = os.path.join(ROOT, 'data-sets', 'shapes')
OUT_DIR = os.path.join(ROOT, 'outputs')
os.makedirs(OUT_DIR, exist_ok=True)


def load_shape_file(path):
    data = np.loadtxt(path)
    if data.shape[1] >= 3:
        coords = data[:, :2]
        labels = data[:, 2].astype(int)
    else:
        coords = data
        labels = None
    return coords, labels


def plot_clusters(X, clusters, centers_idx, outpath, title=None, true_labels=None):
    plt.figure(figsize=(6, 5))
    unique = np.unique(clusters)
    cmap = plt.get_cmap('tab20')
    for i, u in enumerate(unique):
        pts = X[clusters == u]
        plt.scatter(pts[:, 0], pts[:, 1], s=12, color=cmap(i % 20), label=f'c{u}')
    if centers_idx is not None:
        centers = X[centers_idx]
        plt.scatter(centers[:, 0], centers[:, 1], s=80, c='k', marker='x')
    if title:
        plt.title(title)
    if true_labels is not None:
        plt.xlabel('(true labels available)')
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()


def decision_graph(density, delta, centers_idx, outpath, title=None):
    plt.figure(figsize=(6, 4.5))
    plt.scatter(density, delta, s=12)
    if centers_idx is not None:
        plt.scatter(density[centers_idx], delta[centers_idx], s=80, c='r', marker='x')
    plt.xlabel('density')
    plt.ylabel('delta')
    if title:
        plt.title(title)
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()


def compute_density_delta(X):
    # replicate the way DPC.py computes density and delta so we can plot decision graph
    import scipy.spatial.distance as ssd
    N = X.shape[0]
    dist = ssd.pdist(X)
    dmat = ssd.squareform(dist)
    # area used in DPC.py: 2% quantile
    sda = np.sort(dist)
    area = sda[round(sda.shape[0]*2/100)-1]
    density = np.zeros(N, dtype=int)
    for i in range(N-1):
        for j in range(i+1, N):
            if dmat[i, j] < area:
                density[i] += 1
                density[j] += 1
    maxd = dmat.max()
    density_index = np.argsort(-density, kind='stable')
    delta = np.zeros(N, dtype=float)
    delta[density_index[0]] = -1.0
    nneigh = np.zeros(N, dtype=int)
    for i in range(1, N):
        delta[density_index[i]] = maxd
        for j in range(i):
            if dmat[density_index[i], density_index[j]] < delta[density_index[i]]:
                delta[density_index[i]] = dmat[density_index[i], density_index[j]]
                nneigh[density_index[i]] = density_index[j]
    delta[density_index[0]] = delta.max()
    return density, delta


def run():
    datasets = ['R15.txt', 'Aggregation.txt', 'flame.txt', 'T7.10k.txt']
    results = []
    for fname in datasets:
        path = os.path.join(DATA_DIR, fname)
        if not os.path.exists(path):
            print('missing', path)
            continue
        X, labels = load_shape_file(path)
        true_k = len(np.unique(labels)) if labels is not None else None
        k = true_k if true_k is not None else 3

        # run DPC
        clusters = DPC(X, k)

        # clusters in the DPC implementation start at 1; convert to zero-based for plotting
        clusters0 = clusters.copy()

        # compute density and delta for decision graph
        density, delta = compute_density_delta(X)
        gamma = density * delta
        centers_idx = np.argsort(-gamma)[:k]

        base = os.path.splitext(fname)[0]
        plot_clusters(X, clusters0, centers_idx, os.path.join(OUT_DIR, f'{base}_clusters.png'),
                      title=f'{base} - DPC (k={k})', true_labels=labels)
        decision_graph(density, delta, centers_idx, os.path.join(OUT_DIR, f'{base}_decision.png'),
                       title=f'{base} decision graph')

        ari = nmi = None
        if labels is not None:
            ari = adjusted_rand_score(labels, clusters0)
            nmi = normalized_mutual_info_score(labels, clusters0)

        results.append({'dataset': base, 'k': k, 'ari': ari, 'nmi': nmi,
                        'clusters_img': f'{base}_clusters.png', 'decision_img': f'{base}_decision.png'})

        print(f'Ran {fname}: k={k}, ARI={ari}, NMI={nmi}')

    # save results CSV
    import csv
    outcsv = os.path.join(OUT_DIR, 'dpc_results.csv')
    with open(outcsv, 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=['dataset', 'k', 'ari', 'nmi', 'clusters_img', 'decision_img'])
        writer.writeheader()
        for r in results:
            writer.writerow(r)

    print('Outputs saved to', OUT_DIR)


if __name__ == '__main__':
    run()
