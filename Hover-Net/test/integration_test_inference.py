import os
import cv2
import pytest
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from your_project.model import HoverNet  # Replace with your actual model import path
from your_project.inference import run_inference_on_image  # Replace with your inference logic
from your_project.visualization import save_visualization  # Replace with your actual visualization import path

@pytest.fixture
def sample_image():
    # Provide a path to a sample image for inference testing
    image_path = "path/to/sample_image.png"  # Update with a real path
    return image_path

@pytest.fixture
def pretrained_model():
    # Load the pre-trained model
    model_path = "path/to/model_checkpoint.pth"  # Update with the real checkpoint path
    model = HoverNet.load_from_checkpoint(model_path)
    return model

def test_inference_and_visualization(sample_image, pretrained_model):
    output_dir = "visualization/"
    os.makedirs(output_dir, exist_ok=True)
    
    # Run inference
    prediction = run_inference_on_image(pretrained_model, sample_image)
    assert prediction is not None, "Inference failed, no output generated"
    
    # Visualization with legend
    # Load the image
    img = cv2.imread(sample_image)

    # Convert the image to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Create a figure and axis
    plt.figure(figsize=(6, 6))
    plt.imshow(img)

    # Create a legend based on the type_info_dict
    type_info_dict = {
        0: ("nolabe", (0, 0, 0)),        # no label
        1: ("neopla", (255, 0, 0)),      # neoplastic
        2: ("inflam", (0, 255, 0)),      # inflamm
        3: ("connec", (0, 0, 255)),      # connective
        4: ("necros", (255, 255, 0)),    # dead
        5: ("no-neo", (255, 165, 0))     # non-neoplastic epithelial
    }

    # Create patches for each label
    patches = [mpatches.Patch(color=[v/255 for v in color], label=label) 
               for label, color in type_info_dict.values()]

    # Add the legend to the plot
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    # Save the figure with the legend
    output_path = os.path.join(output_dir, "sample_output_with_legend.png")
    plt.savefig(output_path, bbox_inches='tight')

    # Optionally, you can display the plot
    plt.show()
    
    # Ensure output is saved correctly
    assert os.path.exists(output_path), "Output image with legend not saved"

if __name__ == "__main__":
    pytest.main()
