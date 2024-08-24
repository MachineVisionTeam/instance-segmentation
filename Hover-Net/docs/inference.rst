Inference
=========

Running Inference
-----------------
To run inference on new images, use the `inference.ipynb` notebook in the `examples` folder.

Output Interpretation
---------------------
The output is color-coded to represent different nuclei types:

- RED: Neoplastic
- GREEN: Inflammatory
- BLUE: Connective/Soft tissue
- BROWN: Dead
- ORANGE: Epithelial

Usage Example
-------------
1. Open the `inference.ipynb` notebook.
2. Load your trained model located in the `checkpoint` folder at:

   .. code-block:: bash

      /mnt/storage1/hover-net/checkpoint/01/net_epoch=12.tar

3. Prepare your input image by converting `.npy` files to `.jpeg` using the `convert.ipynb` notebook.
4. Run the inference code.
5. Visualize the results using the provided color mapping.

For detailed steps and code, refer to the `inference.ipynb` notebook in the `examples` folder.

Additional Notes
----------------
- Ensure your input images are in the same format as the training data.
- The `convert.ipynb` notebook in the `examples` folder can be used to convert `.npy` files to `.jpeg` format for visualization. The trained input images are in `.npy` files located in the `train` folder. Use `convert.ipynb` to convert these files for use in `inference.ipynb`.
