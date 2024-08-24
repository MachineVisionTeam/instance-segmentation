PanNuke Dataset
===============

Overview
--------
The PanNuke (Pan-Cancer Nuclei) dataset contains semi-automatically generated nuclei instance segmentation and classification images across 19 different tissue types.

Dataset Statistics
------------------
- 481 visual fields
- 205,343 labeled nuclei
- 19 tissue types
- 5 nuclei types
- 312 visual fields randomly sampled from more than 20K whole slide images at different magnifications

Tissue Types
------------
The dataset includes 19 tissue types. The distribution of these types in the dataset is shown in the original dataset documentation.

Nuclei Types
------------
For each tissue type, the dataset includes five nuclei types:

1. Neoplastic
2. Inflammatory
3. Connective/Soft tissue
4. Dead
5. Epithelial

Data Format
-----------
The raw data consists of images and corresponding masks. The `Fold 1` directory is structured as follows:

- `images/` folder: 
  - Contains a `Fold 1` directory.
  - Within this directory, there are two files:
    - `types.npy`: Contains information about the tissue types.
    - `images.npy`: Contains the image data.

- `masks/` folder:
  - Contains a `Fold 1` directory.
  - Within this directory, there is a single file:
    - `masks.npy`: Contains the mask data, including instance segmentation and nuclei classification.

Dataset Analysis
----------------
For a detailed analysis of the dataset, refer to our Jupyter notebook available in the `examples` folder: `HoverNet-data.ipynb`

Significance
------------
Models trained on PanNuke can aid in whole slide image tissue type segmentation and generalize to new tissues, making it a valuable resource for computational pathology research.
