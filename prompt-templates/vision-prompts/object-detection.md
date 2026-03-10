<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Object Detection

I need to implement a real-time object detection system that can process video streams at over 30 FPS. The system should use modern architectures like YOLO, Faster R-CNN, or DETR to detect objects in 640x640 resolution images. I'm working with COCO dataset format and need the model to achieve mAP@0.5 above 0.7. The solution must include visualization capabilities, performance benchmarking, and be deployable to edge devices via ONNX export. Please architect the complete detection pipeline with multi-scale training and optimized NMS.

## Requirements

- Framework: YOLO, Faster R-CNN, or DETR
- Input resolution: 640x640
- Real-time requirement: >30 FPS
- Dataset: COCO or custom annotated data

## Success Criteria

- mAP@0.5 above 0.7
- Multi-scale training implementation
- NMS optimization
- Anchor-free approach consideration

## Deliverables

- Detection model with visualization
- Performance benchmarks
- Export to ONNX format
- Edge deployment ready
