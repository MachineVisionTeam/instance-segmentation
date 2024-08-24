# Tests

This folder contains scripts, configurations, and visualization outputs for testing the HoverNet model pipeline.

## Contents

- **visualization/**: Contains predicted images from inference tests. These visualizations help in reviewing the model's output on test data.
- **test_data_loading.py**: Tests the data loading functions to ensure they work correctly with the PanNuke dataset.
- **integration_test_inference.py**: An end-to-end test that runs inference on a sample image using a pre-trained model, saving the output in the `visualization/` folder.
- **README.md**: This document.

## How to Run the Tests

1. Ensure you have set up the environment and installed the necessary dependencies.
2. Place the trained model checkpoint in the appropriate directory.
3. Run the tests using `pytest` or directly with Python:

   ```bash
   pytest tests/
