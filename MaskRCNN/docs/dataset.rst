=========================
Dataset Preparation Guide
=========================

This document provides instructions on preparing and organizing the NuCLS dataset for training and evaluating the MaskRCNN model. The dataset includes RGB images, corresponding masks, and annotations.

NuCLS Dataset Structure
=======================

The dataset should be organized into the following format:

.. code-block:: text

   /path/to/dataset/
   ├── train/
   │   ├── rgb/
   │   │   ├── image_001.jpg
   │   │   ├── image_002.jpg
   │   │   └── ...
   │   ├── mask/
   │   │   ├── mask_001.png
   │   │   ├── mask_002.png
   │   │   └── ...
   │   └── annotation/
   │       ├── image_001.csv
   │       ├── image_002.csv
   │       └── ...
   ├── val/
   │   ├── rgb/
   │   │   ├── image_103.jpg
   │   │   ├── image_104.jpg
   │   │   └── ...
   │   ├── mask/
   │   │   ├── mask_103.png
   │   │   ├── mask_104.png
   │   │   └── ...
   │   └── annotation/
   │       ├── image_103.csv
   │       ├── image_104.csv
   │       └── ...
   └── test/
       ├── rgb/
       │   ├── image_126.jpg
       │   ├── image_127.jpg
       │   └── ...
       ├── mask/
       │   ├── mask_126.png
       │   ├── mask_127.png
       │   └── ...
       └── annotation/
           ├── image_126.csv
           ├── image_127.csv
           └── ...

Dataset Components
==================

1. **RGB Images**: Stored in the `rgb/` directory under each set (`train`, `val`, `test`). These are the input images in JPG format.
2. **Masks**: Stored in the `mask/` directory under each set (`train`, `val`, `test`). Masks are binary images in PNG format that correspond to each RGB image, where:
   - **0** represents the background.
   - **1** represents the object of interest.
3. **Annotations**: Stored in the `annotation/` directory under each set (`train`, `val`, `test`). Each CSV file contains metadata and annotations related to the corresponding image.

Data Splitting
==============

The dataset is divided into three sets:
- **Training Set**: 102 images for training the model.
- **Validation Set**: 22 images for validating the model during training.
- **Test Set**: 10 images for evaluating the model's performance.

Ensure that the images, masks, and annotations are correctly aligned and named consistently across all sets.

Loading the Dataset
===================

To load the dataset into your MaskRCNN model, you need to modify the data loader script to read from the above directory structure and parse the RGB images, masks, and annotations accordingly.

Ensure that:
- The file paths in your script match the directory structure defined above.
- The script correctly reads and processes the CSV annotations, images, and masks for training, validation, and testing.

Tips for Dataset Preparation
============================

- **Image Quality**: Ensure all images are of high quality and have consistent dimensions.
- **Mask Accuracy**: Masks should precisely represent the object boundaries for accurate training.
- **Annotation Consistency**: Verify that all annotations are correct and consistent across the dataset.
- **Backup Data**: Always keep a backup of your original data files before making any modifications.

By following these guidelines, you will ensure that your dataset is correctly formatted and ready for use with the MaskRCNN model.
