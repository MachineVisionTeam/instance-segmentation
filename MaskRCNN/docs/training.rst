=============================
Training Guide
=============================

This guide provides step-by-step instructions for training the MaskRCNN model on the NuCLS dataset.

Preparing for Training
======================

1. **Prepare the Dataset:**

   Ensure that the dataset is organized as described in `docs/dataset.rst`. The dataset should include RGB images, masks, and annotations properly divided into `train`, `val`, and `test` subdirectories.

2. **Configure the Training Script:**

   Before starting the training, update the parameters in your training script. You can modify the `examples/train.ipynb` notebook directly:

   - **Set `STEPS_PER_EPOCH`**: 
     Adjust the `STEPS_PER_EPOCH` parameter according to the size of your training dataset. For example:
     ```python
     config.STEPS_PER_EPOCH = 100  # Set this based on your dataset size
     ```

   - **Adjust `LEARNING_RATE` and Hyperparameters:**
     Modify the learning rate and other hyperparameters to suit your training needs:
     ```python
     config.LEARNING_RATE = 0.001  # Example value; adjust as needed
     ```

Running the Training Script
===========================

To start the training, run the following command in your terminal:

.. code-block:: bash

   python train.ipynb 

- **`--dataset`**: Path to your dataset directory.
- **`--weights`**: Specify the weights to start with (e.g., `coco` for pre-trained COCO weights).

Saving the Final Model
======================

After the training is complete, the final model weights will be automatically saved in the specified directory as:

.. code-block:: text

   Nucleus_MaskRCNN_100epochs_final.h5

Make sure to use this file for inference or further evaluation of your model.

Tips for Effective Training
===========================

- **Start with Pre-trained Weights**: Utilize pre-trained weights like COCO for better initial performance.
- **Fine-tune Hyperparameters**: Experiment with different hyperparameters, such as learning rates and batch sizes, to find the best configuration for your dataset.
- **Use GPU for Training**: Ensure you are using a GPU to significantly reduce training time.

By following these steps, you can effectively train your MaskRCNN model on the NuCLS dataset.
