# Fashion-MNIST ANN Pipeline with Git, DVC & Google Drive

## Project Overview
This repository implements an end-to-end Machine Learning versioning pipeline for classifying the **Fashion-MNIST** dataset using a fully-connected Artificial Neural Network (ANN) in TensorFlow.

The project demonstrates:
- **Advanced Git Workflows**: Feature branching, log variants, diff variants, stashing, rebasing, resetting, and conflict resolution.
- **Data & Model Versioning with DVC**: Versioning large datasets (`data/raw`, `data/processed`) and model artifacts (`models/model.h5`) using a Google Drive remote.
- **Reproducible ML Pipeline**: Orchestration via `dvc.yaml` and single-source-of-truth hyperparameters configured in `params.yaml`.
- **Target Performance**: Exceeded requirement with **88.17%** test accuracy.

## Deliverables & Links
- **GitHub Repository**: [Anasnaveed69/fashion-ann-pipeline](https://github.com/Anasnaveed69/fashion-ann-pipeline)
- **Google Drive Remote Storage**: [DVC Shared Remote Folder](https://drive.google.com/drive/folders/1ke8PvXC583PccUvoobOeMrqiywJFURZP?usp=sharing)
- **Official Assignment Report**: [`Assignment3_ML_Versioning_23L-0764.pdf`](./Assignment3_ML_Versioning_23L-0764.pdf)

## Project Structure
```text
fashion-ann-pipeline/
├── .dvc/                   # DVC configuration and metadata
├── data/
│   ├── raw/                # Fashion-MNIST raw arrays (DVC tracked)
│   └── processed/          # Normalized & train/val split arrays (DVC tracked)
├── models/                 # Trained model weights, confusion matrix & history (DVC tracked)
├── src/
│   ├── prepare.py          # Downloads & saves raw Fashion-MNIST
│   ├── preprocess.py       # Normalizes pixel values and creates validation split
│   ├── train.py            # Builds and trains the ANN model
│   └── evaluate.py         # Evaluates model, plots confusion matrix, writes metrics
├── dvc.yaml                # DVC multi-stage pipeline definition
├── dvc.lock                # Pipeline reproducibility lock file
├── params.yaml             # Hyperparameters single source of truth
├── metrics.json            # Model evaluation metrics (test accuracy & loss)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Model Performance & Version Comparison

| Pipeline Version | Dense Units | Dropout | Epochs | Test Loss | Test Accuracy | Git Tag | DVC Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **v1 (Baseline)** | 128 | 0.20 | 10 | 0.3641 | **87.02%** | `v1` | Synced |
| **v2 (Tuned)** | 256 | 0.20 | 10 | 0.3435 | **88.17% (+1.15%)** | `v2` | Synced |

## Quick Start & Reproduction

1. **Clone repository**:
   ```bash
   git clone https://github.com/Anasnaveed69/fashion-ann-pipeline.git
   cd fashion-ann-pipeline
   ```
2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Pull Data & Model Artifacts from Google Drive**:
   ```bash
   dvc pull
   ```
4. **Reproduce Pipeline End-to-End**:
   ```bash
   dvc repro
   ```

<!-- Hotfix: verified environment requirements and seed reproduction -->
