"""Model evaluation script for Fashion-MNIST ANN pipeline.

Loads the trained model from models/model.h5 and the processed test set from data/processed/.
Computes test loss and accuracy, generates a styled confusion matrix plot,
and writes the evaluation metrics to metrics.json at the project root.
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import tensorflow as tf


CLASS_NAMES = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot"
]


def plot_confusion_matrix(
    cm: np.ndarray,
    classes: list,
    save_path: str = os.path.join("models", "confusion_matrix.png")
) -> None:
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(9, 7), dpi=150)
    plt.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
    plt.title("Fashion-MNIST ANN Confusion Matrix", fontsize=14, pad=15)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45, ha="right", fontsize=9)
    plt.yticks(tick_marks, classes, fontsize=9)

    # Label values in cells
    thresh = cm.max() / 2.0
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(
                j,
                i,
                f"{cm[i, j]}",
                horizontalalignment="center",
                verticalalignment="center",
                color="white" if cm[i, j] > thresh else "black",
                fontsize=8
            )

    plt.ylabel("True Label", fontsize=11)
    plt.xlabel("Predicted Label", fontsize=11)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[EVALUATE] Confusion matrix saved to: {save_path}")


def evaluate_model(
    model_path: str = os.path.join("models", "model.h5"),
    processed_dir: str = os.path.join("data", "processed"),
    metrics_path: str = "metrics.json"
) -> None:
    print(f"[EVALUATE] Loading model from: {model_path}")
    model = tf.keras.models.load_model(model_path)

    print(f"[EVALUATE] Loading test data from: {processed_dir}")
    x_test = np.load(os.path.join(processed_dir, "X_test.npy"))
    y_test = np.load(os.path.join(processed_dir, "y_test.npy"))

    print(f"[EVALUATE] Evaluating model on test set...")
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    print(f"[EVALUATE] Test Loss: {loss:.4f} | Test Accuracy: {accuracy * 100:.2f}%")

    y_pred_probs = model.predict(x_test, verbose=0)
    y_pred = np.argmax(y_pred_probs, axis=1)

    cm = confusion_matrix(y_test, y_pred)
    plot_confusion_matrix(cm, CLASS_NAMES)

    metrics = {
        "test_loss": round(float(loss), 4),
        "test_accuracy": round(float(accuracy), 4)
    }

    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)
    print(f"[EVALUATE] Metrics written to {metrics_path}: {metrics}")


if __name__ == "__main__":
    evaluate_model()
