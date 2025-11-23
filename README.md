# DataWarehouse_and_DataMining

Summary
- Repository containing code, notebooks, and notes related to data warehousing, ETL/ELT pipelines, dimensional modeling, OLAP analysis, and data mining algorithms (classification, clustering, association rules, anomaly detection).

Contents
- /etl/ — ETL scripts and pipeline examples
- /dwh/ — Data warehouse schema (star/snowflake) examples and DDL
- /notebooks/ — Exploratory and tutorial notebooks
- /models/ — Training and evaluation scripts for data mining models
- /data/ — Sample datasets or links (large files excluded)
- README.md — This file

Quick start
1. Clone repository
    ```bash
    git clone https://github.com/IMNJL/DataWarehouse_and_DataMining
    cd DataWarehouse_and_DataMining
    ```
2. Create environment
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # macOS/Linux
    .venv\Scripts\activate      # Windows
    pip install -r requirements.txt
    ```
3. Run examples
    - Launch Jupyter:
      ```bash
      jupyter lab
      ```
    - Run an ETL script:
      ```bash
      python etl/load_sales.py --config configs/dev.yaml
      ```

Examples (concepts)
- Dimensional modeling: star schema with fact_sales and dimension tables (dim_date, dim_customer, dim_product)
- ETL pattern: extract (CSV/DB), transform (cleaning, joins, SCD handling), load (bulk insert/merge)
- OLAP: aggregated cubes by date, product, region
- Data mining: sample notebooks for k-means, decision trees, random forest, apriori association rules, anomaly detection

Project structure (generated from repository)
```
├─ DWH_1_Detecting_novel_associations_in_large_data_sets/
│  ├─ README.md
│  ├─ requirements.txt
│  ├─ Detecting-Novel-Associations-in-Large-Data-Sets.pptx
│  ├─ slides_text.md
│  ├─ env/
│  │  ├─ bin/
│  │  ├─ include/
│  │  ├─ lib/
│  │  ├─ pyvenv.cfg
│  │  └─ share/
│  ├─ outputs/
│  │  ├─ experiment_results.csv
│  │  └─ (plots .png)
│  ├─ src/
│  │  ├─ __init__.py
│  │  ├─ experiments.py
│  │  ├─ make_presentation.py
│  │  ├─ mic_demo.py
│  │  └─ mic_utils.py
│  └─ tests/
│     └─ test_mic.py
├─ DWH_2_Clustering_by_fast_search_and_find_of_density_peaks/
│  └─ {project_structure}
├─ DWH_3_How_to_improve_the_accuracy_of_clustering_algorithms/
│  ├─ DPC.py
│  ├─ HIAC.py
│  ├─ DWH_3.pptx
│  ├─ DWH_3_HIAC_experiment_report.md
│  ├─ LICENSE
│  ├─ README.md
│  ├─ parameter-config.xls
│  ├─ Wireless_indoor_location/
│  │  ├─ Wireless_indoor_location_after_pca.png
│  │  └─ Wireless_indoor_location_normalization.txt
│  ├─ data-sets/
│  │  ├─ A-set/
│  │  ├─ Adj/
│  │  ├─ S-set/
│  │  ├─ dimension/
│  │  ├─ noise-datasets/
│  │  ├─ real-datasets/
│  │  └─ shapes/
│  └─ figures/
│     └─ README.md
├─ exam/
│  ├─ Data Warehouse and Data Mining.md
│  └─ Data_Warehouse_and_Data_Mining.tex
├─ README.md
```

Contributing
- Open issues for bugs or feature requests
- Create pull requests with tests and documentation updates

License
- Specify a license in LICENSE (e.g., MIT)

Contact
- Add maintainer/contact info in repository settings or CONTRIBUTORS file