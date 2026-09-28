# Fashion-MNIST ANN Pipeline with Git, DVC & Google Drive

## Project Overview
This repository implements an end-to-end Machine Learning versioning pipeline for classifying the **Fashion-MNIST** dataset using a fully-connected Artificial Neural Network (ANN) in TensorFlow.

The project demonstrates:
- **Advanced Git Workflows**: Feature branching, log and diff variants, stashing, rebasing, resetting, and conflict resolution.
- **Data & Model Versioning with DVC**: Versioning large datasets (`data/raw`, `data/processed`) and model artifacts (`models/model.h5`) using a Google Drive remote.
- **Reproducible ML Pipeline**: Orchestration via `dvc.yaml` and single-source-of-truth hyperparameters configured in `params.yaml`.
- **Target Performance**: Achieving $\ge 85\%$ test accuracy on Fashion-MNIST classification.

## Project Structure
```text
fashion-ann-pipeline/
├── .dvc/                   # DVC configuration and metadata
├── data/
│   ├── raw/                # Fashion-MNIST raw arrays (DVC tracked)
│   └── processed/          # Normalized & train/val split arrays (DVC tracked)
├── models/                 # Trained model weights & training history (DVC tracked)
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

## Quick Start
1. **Clone repository**:
   ```bash
   git clone https://github.com/Anasnaveed69/fashion-ann-pipeline.git
   cd fashion-ann-pipeline
   ```
2. **Set up environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Reproduce Pipeline**:
   ```bash
   dvc repro
   ```

<!-- Hotfix: verified environment requirements and seed reproduction -->

