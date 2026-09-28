"""Data preprocessing script for Fashion-MNIST pipeline.

Loads raw arrays, normalizes pixel intensities to [0, 1], and splits a validation
set out of the training data using parameters defined in params.yaml.
"""

import os
import yaml
import numpy as np
from sklearn.model_selection import train_test_split


def load_params(params_path: str = "params.yaml") -> dict:
    if os.path.exists(params_path):
        with open(params_path, "r") as f:
            params = yaml.safe_load(f)
            return params.get("preprocess", {})
    return {"test_size": 0.2, "seed": 42}


def preprocess_data(
    raw_dir: str = os.path.join("data", "raw"),
    processed_dir: str = os.path.join("data", "processed"),
    params_path: str = "params.yaml"
) -> None:
    params = load_params(params_path)
    val_size = params.get("test_size", 0.2)
    seed = params.get("seed", 42)

    os.makedirs(processed_dir, exist_ok=True)
    print(f"[PREPROCESS] Loading raw data from: {raw_dir}")
    train_images = np.load(os.path.join(raw_dir, "train_images.npy"))
    train_labels = np.load(os.path.join(raw_dir, "train_labels.npy"))
    test_images = np.load(os.path.join(raw_dir, "test_images.npy"))
    test_labels = np.load(os.path.join(raw_dir, "test_labels.npy"))

    # Reconciled Normalization Strategy: Supports both standard [0, 1] scaling and z-score
    normalization_mode = params.get("normalization", "standard")
    if normalization_mode == "zscore":
        print(f"[PREPROCESS] Reconciled normalization: Z-score standardization (mean=0, std=1)...")
        mean_val = np.mean(train_images.astype(np.float32))
        std_val = np.std(train_images.astype(np.float32)) + 1e-7
        x_train_norm = (train_images.astype(np.float32) - mean_val) / std_val
        x_test_norm = (test_images.astype(np.float32) - mean_val) / std_val
    else:
        print(f"[PREPROCESS] Reconciled normalization: Standard scaling to [0.0, 1.0]...")
        x_train_norm = train_images.astype(np.float32) / 255.0
        x_test_norm = test_images.astype(np.float32) / 255.0

    print(f"[PREPROCESS] Splitting validation set (val_size={val_size}, seed={seed})...")
    x_train_split, x_val_split, y_train_split, y_val_split = train_test_split(
        x_train_norm,
        train_labels,
        test_size=val_size,
        random_state=seed,
        stratify=train_labels
    )

    np.save(os.path.join(processed_dir, "X_train.npy"), x_train_split)
    np.save(os.path.join(processed_dir, "y_train.npy"), y_train_split)
    np.save(os.path.join(processed_dir, "X_val.npy"), x_val_split)
    np.save(os.path.join(processed_dir, "y_val.npy"), y_val_split)
    np.save(os.path.join(processed_dir, "X_test.npy"), x_test_norm)
    np.save(os.path.join(processed_dir, "y_test.npy"), test_labels)

    print(f"[PREPROCESS] Processed data saved successfully to: {processed_dir}")
    print(f"             - X_train: {x_train_split.shape}, y_train: {y_train_split.shape}")
    print(f"             - X_val:   {x_val_split.shape}, y_val:   {y_val_split.shape}")
    print(f"             - X_test:  {x_test_norm.shape}, y_test:  {test_labels.shape}")


if __name__ == "__main__":
    preprocess_data()
