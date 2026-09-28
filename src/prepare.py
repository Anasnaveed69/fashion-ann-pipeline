"""Data preparation script for Fashion-MNIST pipeline.

Downloads the Fashion-MNIST dataset from keras.datasets and saves the
raw training and testing images and labels as NumPy arrays under data/raw/.
"""

import os
import numpy as np
import tensorflow as tf


def prepare_data(output_dir: str = os.path.join("data", "raw")) -> None:
    os.makedirs(output_dir, exist_ok=True)
    print(f"[PREPARE] Downloading Fashion-MNIST dataset...")
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

    train_images_path = os.path.join(output_dir, "train_images.npy")
    train_labels_path = os.path.join(output_dir, "train_labels.npy")
    test_images_path = os.path.join(output_dir, "test_images.npy")
    test_labels_path = os.path.join(output_dir, "test_labels.npy")

    np.save(train_images_path, x_train)
    np.save(train_labels_path, y_train)
    np.save(test_images_path, x_test)
    np.save(test_labels_path, y_test)

    print(f"[PREPARE] Raw data successfully saved to: {output_dir}")
    print(f"          - Train images: {x_train.shape}, Labels: {y_train.shape}")
    print(f"          - Test images:  {x_test.shape}, Labels: {y_test.shape}")


if __name__ == "__main__":
    prepare_data()
