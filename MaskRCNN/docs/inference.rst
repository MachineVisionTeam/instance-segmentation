============================
Inference Guide
============================

This guide provides instructions on how to perform inference using the trained MaskRCNN model on the NuCLS dataset.

Preparing for Inference
=======================

1. **Prepare the Test Dataset:**

   Ensure that your test data is correctly organized as described in `docs/dataset.rst`. The test dataset should include RGB images, masks, and annotations properly placed in the `/test/` subdirectory.

Running the Inference Script
============================

To perform inference on the test dataset using the trained MaskRCNN model, run the following command in your terminal:

.. code-block:: bash

   python predict.ipynb  
- **`--model_path`**: The path to the trained model weights file (e.g., `Nucleus_MaskRCNN_100epochs_final.h5`).
- **`--image_path`**: The path to the test image or a directory containing test images.

Visualizing Results
===================

The inference script will generate images with predicted masks and save them in the specified output directory. By default, the output is saved to:

.. code-block:: text

   /home/skoganti/sample/Sample/MaskRCNN/output_predictions1/

Make sure to check this directory for the visualized results.

Evaluating the Model
====================

After performing inference, the script will compute evaluation metrics such as Precision, Recall, and F1 Score using Intersection over Union (IoU) thresholds. The results will be saved in the output directory for further analysis.

For more detailed information on running inference, refer to the `examples/inference.ipynb` notebook.

Additional Notes
================

- **Ensure Compatibility**: Verify that all dependencies are correctly installed and compatible with your system configuration.
- **Modify Paths as Needed**: Make sure to replace the placeholder paths (`/path/to/...`) with actual paths on your system.
- **Use GPU for Faster Inference**: If available, run inference on a GPU for faster processing.

By following these instructions, you will be able to successfully perform inference with the trained MaskRCNN model on the NuCLS dataset.
