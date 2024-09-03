import os
import numpy as np
import matplotlib.pyplot as plt
from mrcnn.model import MaskRCNN
from inference import InferenceConfig
from nucleus_dataset import NucleusDataset
from mrcnn import visualize, utils
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
test_dataset = NucleusDataset()
test_dataset.load_test_dataset(dataset_dir='/home/skoganti/sample/Sample/MaskRCNN/test_main')
test_dataset.prepare()
output_dir = "/home/skoganti/sample/Sample/MaskRCNN/output_predictions1"
os.makedirs(output_dir, exist_ok=True)
model_path = "Nucleus_MaskRCNN_100epochs_final.h5"
model = MaskRCNN(mode="inference", config=InferenceConfig(), model_dir="/home/skoganti/sample/Sample/MaskRCNN")
model.load_weights(model_path, by_name=True)
ious = []
precisions = []
recalls = []
f1_scores = []
for image_id in test_dataset.image_ids:
    original_image, image_meta, gt_class_id, gt_bbox, gt_mask = \
        mrcnn.model.load_image_gt(test_dataset, InferenceConfig(), image_id, use_mini_mask=False)
    results = model.detect([original_image], verbose=1)
    r = results[0]
    plt.figure(figsize=(8, 8))
    visualize.display_instances(original_image, r['rois'], r['masks'], r['class_ids'], test_dataset.class_names, r['scores'], figsize=(8, 8), show_bbox=True, show_mask=True, title="Predictions")
    pred_image_path = os.path.join(output_dir, f"predictions_{image_id}.png")
    plt.savefig(pred_image_path, dpi=300, bbox_inches='tight')
    plt.close()
    gt_bboxes = gt_bbox
    pred_bboxes = r['rois']
    def calculate_iou(box1, box2):
        y1, x1, y2, x2 = box1
        y1_b, x1_b, y2_b, x2_b = box2
        xi1 = max(x1, x1_b)
        yi1 = max(y1, y1_b)
        xi2 = min(x2, x2_b)
        yi2 = min(y2, y2_b)
        inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
        box1_area = (x2 - x1) * (y2 - y1)
        box2_area = (x2_b - x1_b) * (y2_b - y1_b)
        union_area = box1_area + box2_area - inter_area
        iou = inter_area / union_area
        return iou
    ious = [max(calculate_iou(pred_box, gt_box) for gt_box in gt_bboxes) for pred_box in pred_bboxes]
    IOU_THRESHOLD = 0.5
    tp = sum([1 for iou in ious if iou >= IOU_THRESHOLD])
    fp = len(pred_bboxes) - tp
    fn = len(gt_bboxes) - tp
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    precisions.append(precision)
    recalls.append(recall)
    f1_scores.append(f1)
    print(f"Image {image_id} - Precision: {precision:.4f}, Recall: {recall:.4f}, F1 Score: {f1:.4f}")
