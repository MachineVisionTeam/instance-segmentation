Installation
============

This document provides instructions for setting up the HoverNet project for the PanNuke dataset.

Dependencies
------------
- PyTorch
- NumPy
- tqdm
- Matplotlib
- Jupyter Notebook

Installation Steps
------------------
1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/vqdang/hover_net.git
      cd hover_net

2. Set up a Conda environment with Python 3.7.12:

   .. code-block:: bash

      conda create -n new_hovernet python=3.7.12
      conda activate new_hovernet

3. Install the required dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Install PyTorch with CUDA 11.5 support:

   .. code-block:: bash

      pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu115

5. Download the PanNuke dataset:
   The Fold 1 of the dataset is hosted on TIA Center. You can download it from:
   `https://warwick.ac.uk/fac/cross_fac/tia/data/pannuke <https://warwick.ac.uk/fac/cross_fac/tia/data/pannuke>`_

6. Set up the dataset:
   Place the downloaded dataset in the `Fold 1` directory of the project.

Your environment is now set up and ready to use.
