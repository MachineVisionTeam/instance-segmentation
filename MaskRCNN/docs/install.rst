===============================
Installation Instructions
===============================

This guide provides step-by-step instructions for setting up the environment to run the MaskRCNN model with the NuCLS dataset.

Prerequisites
=============

- **Python 3.7.3**: Make sure to install Python 3.7.3. You can download it from [python.org](https://www.python.org/downloads/release/python-373/).

Step-by-Step Installation
=========================

1. **Clone the Repository**

   Start by cloning the GitHub repository to your local machine:

   .. code-block:: bash

      git clone https://github.com/MachineVisionTeam/instance-segmentation/edit/main/MaskRCNN.git
      cd MaskRCNN

2. **Create a Python Virtual Environment**

   Create a Python virtual environment using Python 3.7.3:

   .. code-block:: bash

      python3.7 -m venv maskrcnn-env
      source maskrcnn-env/bin/activate  # For Linux/macOS
      maskrcnn-env\Scripts\activate  # For Windows

   This step creates an isolated environment to manage dependencies without interfering with your system Python packages.

3. **Upgrade pip and setuptools**

   Make sure you have the latest versions of `pip` and `setuptools`:

   .. code-block:: bash

      pip install --upgrade pip setuptools

4. **Install Required Dependencies**

   Install all the necessary Python packages:

   .. code-block:: bash

      pip install absl-py==2.1.0 astor==0.8.1 attrs==23.2.0 cachetools==4.2.4 certifi==2024.2.2 charset-normalizer==3.3.2 cycler==0.11.0 decorator==5.1.1 flatbuffers==24.3.25 fonttools==4.38.0 gast==0.2.2 google-auth==1.35.0 google-auth-oauthlib==0.4.6 google-pasta==0.2.0 grpcio==1.62.2 h5py==2.10.0 idna==3.7 imageio==2.31.2 importlib-metadata==6.7.0 Keras==2.2.5 Keras-Applications==1.0.8 Keras-Preprocessing==1.1.2 kiwisolver==1.4.5 Markdown==3.4.4 matplotlib==3.1.1 networkx==2.6.3 numpy==1.17.0 opencv-python==4.9.0.80 opt-einsum==3.3.0 pandas==1.2.0 Pillow==9.5.0 protobuf==3.20.0 PyWavelets==1.3.0 PyYAML==6.0.1 requests==2.31.0 rsa==4.9 scikit-image==0.15.0 scikit-learn==1.0.2 scipy==1.4.1 six==1.16.0 tensorboard==1.15.0 tensorflow==1.15.5 tensorflow-estimator==1.15.1 tensorflow-gpu==1.15.5 termcolor==2.3.0 threadpoolctl==3.1.0 Werkzeug==2.2.3 wrapt==1.16.0

   > **Note:** This list includes essential packages required for the project. Adjust as necessary based on your specific environment or use case.

5. **Download Pretrained MaskRCNN COCO Weights**

   The MaskRCNN model requires pretrained weights to run correctly. Follow these steps to download the weights:

   - Open the following link: [Mask RCNN COCO weights v2.0](https://github.com/matterport/Mask_RCNN/releases/tag/v2.0)
   - Scroll down to "Assets" and expand it.
   - Download the file named `mask_rcnn_coco.h5`.
   - Place the downloaded file in the `mask_rcnn` directory of the repository.

6. **Prepare the NuCLS Dataset**

   Download and organize the NuCLS dataset as described in the `docs/dataset.rst` file. Make sure the dataset is properly formatted and placed in the correct directory.

Additional Configuration
========================

Some additional configuration may be necessary depending on your hardware and operating system:

- **CUDA and cuDNN**: Ensure that CUDA 10.0 and cuDNN 7.4 are installed for TensorFlow GPU 1.15.5 to work correctly.
- **Graphics Drivers**: Update your graphics drivers to the latest version that supports CUDA 10.0.

Environment Variables
======================

Make sure to set the following environment variables:

.. code-block:: bash

   export CUDA_HOME=/usr/local/cuda-10.0
   export PATH=$CUDA_HOME/bin:$PATH
   export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

These settings help TensorFlow recognize your GPU for accelerated computing.

Next Steps
==========

Once the installation is complete, you can proceed with the following:

- **Training the Model**: See `docs/training.rst` for instructions on training the MaskRCNN model.
- **Running Inference**: See `docs/inference.rst` for details on running inference using the trained model.

Troubleshooting
===============

If you encounter issues during installation:

- **Check Python Version**: Ensure you are using Python 3.7.3.
- **Dependency Conflicts**: Review the list of installed packages and resolve any version conflicts.
- **CUDA Compatibility**: Verify that your CUDA version matches the required TensorFlow GPU version.



