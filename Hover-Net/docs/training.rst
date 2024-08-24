Training HoverNet
=================

Setup
-----
1. Ensure you have prepared the data as described in `HoverNet-data.ipynb`.
2. Download the model checkpoint trained on the PanNuke dataset from:

   `https://drive.google.com/file/d/1SbSArI3KOOWHxRlxnjchO7_MbWzB4lNR/view`.

3. Configure the training parameters in the HoverNet configuration file.

Configuration
-------------
Modify the HoverNet configuration file to match your PanNuke dataset setup. Key parameters to adjust include:
- Data paths
- Number of epochs
- Batch size
- Learning rate

Running Training
----------------
To start training, you can run the `HoverNet-train.ipynb` notebook. Inside this notebook, you will find the command:

   .. code-block:: bash

      !python run_train.py --gpu='0'

This command will execute the training code, utilizing the datasets located in the `train` and `val` folders that were set up through `HoverNet-data.ipynb`, and using the downloaded model checkpoint.

Validation Results
------------------
After training, you should see validation results similar to:

- valid-np_acc : 0.94211
- valid-np_dice : 0.83099
- valid-tp_dice_0 : 0.96235
- valid-tp_dice_1 : 0.63813
- valid-tp_dice_2 : 0.55646
- valid-tp_dice_3 : 0.46966
- valid-tp_dice_4 : 0.00026
- valid-tp_dice_5 : 0.06760
- valid-hv_mse : 0.04192

Interpreting Results
--------------------
- np_acc: Nuclear pixel accuracy
- np_dice: Dice coefficient for nuclear pixels
- tp_dice_X: Dice coefficient for each nuclei type
- hv_mse: Mean squared error for the horizontal and vertical maps

Higher values indicate better performance for accuracy and Dice coefficients, while lower values are better for MSE.

For detailed training process and results, refer to the `HoverNet-train.ipynb` notebook in the `examples` folder.
