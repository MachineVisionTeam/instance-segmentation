import os
import numpy as np
import matplotlib.pyplot as plt
from mrcnn.model import MaskRCNN
from inference import InferenceConfig
from nucleus_dataset import NucleusDataset
from mrcnn import visualize
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
test_dataset = NucleusDataset()
test_dataset.load_test_dataset(dataset_dir='/home/skoganti/sample/Sample/MaskRCNN/test_main')
test_dataset.prepare()
output_dir = "/home/skoganti/sample/Sample/MaskRCNN/output_predictions1"
os.makedirs(output_dir, exist_ok=True)
model_path = "Nucleus_MaskRCNN_100epochs_final.h5"
model = MaskRCNN(mode="inference", config=InferenceConfig(), model_dir="/home/skoganti/sample/Sample/MaskRCNN")
model.load_weights(model_path, by_name=True)
image_id = 0  # Adjust this index based on your dataset
original_image, image_meta, gt_class_id, gt_bbox, gt_mask = \
    mrcnn.model.load_image_gt(test_dataset, InferenceConfig(), image_id, use_mini_mask=False)
results = model.detect([original_image], verbose=1)
r = results[0]
plt.figure(figsize=(8, 8))
visualize.display_instances(original_image, r['rois'], r['masks'], r['class_ids'], test_dataset.class_names, r['scores'], figsize=(8, 8), show_bbox=True, show_mask=True, title="Predictions")
pred_image_path = os.path.join(output_dir, f"predictions_{image_id}.png")
plt.savefig(pred_image_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Predictions for image {image_id} have been saved to {pred_image_path}")
