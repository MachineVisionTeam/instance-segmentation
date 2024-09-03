===========================
MaskRCNN Model Description
===========================

The MaskRCNN model is designed for instance segmentation of nuclei in histopathology images. This implementation is customized to work with the NuCLS dataset, which includes various classes of nuclei, such as tumor, fibroblast, lymphocyte, and others.

**Model Architecture:**
- Base model: MaskRCNN
- Backbone: ResNet101
- Number of Classes: 14 (including the background)

**Custom Modifications:**
- Added support for 13 different types of nuclei as defined in the NuCLS dataset.
- Configurations optimized for training on histopathology images.

**Model Configuration:**
Refer to the `NucleusConfig` class in the training script to see all the hyperparameters, such as:
- `GPU_COUNT = 1`
- `IMAGES_PER_GPU = 1`
- `NUM_CLASSES = 14`

**Training and Inference:**
See `docs/training.rst` for training details and `docs/inference.rst` for inference guidelines.
