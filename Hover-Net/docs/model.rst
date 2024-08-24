HoverNet Model
==============

Overview
--------
HoverNet is an instance segmentation model designed for computational pathology, making it particularly suitable for the PanNuke dataset.

Architecture
------------
HoverNet is designed to perform simultaneous nuclear instance segmentation and classification. Its architecture is optimized for processing histopathology images.

Input Format
------------
The model expects input in the format:
(items, img_size, img_size, indices)

Where:
- items: number of images
- img_size: 256 (for 256x256 images)
- indices:
  - 0:3 are RGB channels
  - 3 is the instance segmentation
  - 4 is the nuclei classification

Output Format
-------------
The model outputs instance segmentation masks and nuclei type classifications.

Official Implementation
-----------------------
We use the official HoverNet implementation available at:
https://github.com/vqdang/hover_net

For our specific implementation and usage, refer to the training and inference documentation.
