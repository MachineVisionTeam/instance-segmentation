import os
import numpy as np

def test_data_loading():
    # Define the paths to the dataset
    train_images_path = 'path_to_your_train_images.npy'
    train_masks_path = 'path_to_your_train_masks.npy'

    # Check if the paths exist
    assert os.path.exists(train_images_path), f"Training images path does not exist: {train_images_path}"
    assert os.path.exists(train_masks_path), f"Training masks path does not exist: {train_masks_path}"

    # Load the images and masks
    images = np.load(train_images_path)
    masks = np.load(train_masks_path)

    # Verify that images and masks have the same length
    assert len(images) == len(masks), "Mismatch between number of images and masks"

    # Additional checks can be added here, such as shape or data type checks
    print("Data loading test passed.")

if __name__ == "__main__":
    test_data_loading()
