"""Model training script for Fashion-MNIST ANN pipeline.

Builds a fully-connected Artificial Neural Network (ANN) using Keras Sequential API:
Flatten -> Dense (ReLU) -> Dropout -> Dense(10, Softmax).
Compiles with Adam optimizer and sparse_categorical_crossentropy loss.
Trains on data/processed/ and saves models/model.h5 and models/history.csv.
"""

import os
import csv
import yaml
import numpy as np
import tensorflow as tf


def load_params(params_path: str = "params.yaml") -> dict:
    if os.path.exists(params_path):
        with open(params_path, "r") as f:
            params = yaml.safe_load(f)
            return params.get("train", {})
    return {
        "dense_units": 128,
        "dropout_rate": 0.2,
        "learning_rate": 0.001,
        "epochs": 10,
        "batch_size": 64
    }


def train_model(
    processed_dir: str = os.path.join("data", "processed"),
    models_dir: str = "models",
    params_path: str = "params.yaml"
) -> None:
    params = load_params(params_path)
    dense_units = int(params.get("dense_units", 128))
    dropout_rate = float(params.get("dropout_rate", 0.2))
    learning_rate = float(params.get("learning_rate", 0.001))
    epochs = int(params.get("epochs", 10))
    batch_size = int(params.get("batch_size", 64))

    os.makedirs(models_dir, exist_ok=True)

    print(f"[TRAIN] Loading processed arrays from: {processed_dir}")
    x_train = np.load(os.path.join(processed_dir, "X_train.npy"))
    y_train = np.load(os.path.join(processed_dir, "y_train.npy"))
    x_val = np.load(os.path.join(processed_dir, "X_val.npy"))
    y_val = np.load(os.path.join(processed_dir, "y_val.npy"))

    print(f"[TRAIN] Building ANN model:")
    print(f"        - Flatten (input_shape=(28, 28))")
    print(f"        - Dense ({dense_units}, activation='relu')")
    print(f"        - Dropout ({dropout_rate})")
    print(f"        - Dense (10, activation='softmax')")

    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28), name="flatten_input"),
        tf.keras.layers.Dense(dense_units, activation="relu", name="dense_hidden"),
        tf.keras.layers.Dropout(dropout_rate, name="dropout"),
        tf.keras.layers.Dense(10, activation="softmax", name="dense_output")
    ])

    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(
        optimizer=optimizer,
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    model.summary()

    print(f"[TRAIN] Training ANN for {epochs} epochs with batch size {batch_size}...")
    history = model.fit(
        x_train,
        y_train,
        validation_data=(x_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        verbose=1
    )

    # Save trained model to models/model.h5
    model_save_path = os.path.join(models_dir, "model.h5")
    model.save(model_save_path)
    print(f"[TRAIN] Model saved successfully to: {model_save_path}")

    # Save training history to models/history.csv
    history_save_path = os.path.join(models_dir, "history.csv")
    keys = list(history.history.keys())
    with open(history_save_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(keys)
        num_epochs = len(history.history[keys[0]])
        for i in range(num_epochs):
            writer.writerow([history.history[k][i] for k in keys])
    print(f"[TRAIN] Training history saved to: {history_save_path}")


if __name__ == "__main__":
    train_model()
