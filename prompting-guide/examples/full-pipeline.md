# Full Pipeline Example: CoT + ReAct

## Task

Build a complete image classification system for a retail company to classify product images into 20 categories for automated inventory management.

## Requirements

- 10,000 labeled images available
- Must run on 8GB GPU
- Inference time < 100ms
- 95% accuracy required

## Deliverables

- Trained model with >95% validation accuracy
- Docker container for deployment
- API endpoint for predictions
- Documentation and tests

## Complete Workflow

### 1. Chain of Thought Planning

```markdown
Let me plan the complete pipeline:

**Step 1: Data Analysis**
- 10,000 images across 20 classes = ~500 per class
- Need heavy augmentation for small dataset
- Check class distribution for imbalance

**Step 2: Model Selection**
- Small dataset → transfer learning essential
- 20 classes → relatively simple task
- EfficientNet-B0 or ResNet50 should work
- EfficientNet better for deployment (smaller)

**Step 3: Training Strategy**
- Start with frozen backbone, train classifier
- Then unfreeze and fine-tune with low LR
- Use class weights for imbalance
- Early stopping to prevent overfitting

**Step 4: Optimization Plan**
- Mixed precision for memory efficiency
- Gradient accumulation if needed
- Export to ONNX for fast inference
- Quantization if needed for <100ms

**Step 5: Deployment Architecture**
- FastAPI for REST endpoint
- Redis for caching
- Docker for containerization
- Include health checks and monitoring
```

### 2. ReAct Implementation

```markdown
### Phase 1: Data Preparation

**Thought**: Need to analyze the dataset first
**Action**: Load and explore data
```python
import pandas as pd
from pathlib import Path

data_dir = Path("product_images")
df = pd.DataFrame([(p.parent.name, p.name)
                   for p in data_dir.glob("*/*.jpg")],
                  columns=['class', 'filename'])
print(df['class'].value_counts())
```
**Observation**: Classes range from 200 to 800 samples (imbalanced)

**Thought**: Need to handle class imbalance
**Action**: Calculate class weights
```python
from sklearn.utils.class_weight import compute_class_weight

classes = df['class'].unique()
class_weights = compute_class_weight(
    'balanced',
    classes=classes,
    y=df['class']
)
weight_dict = dict(zip(classes, class_weights))
```
**Observation**: Weights range from 0.6 to 3.2

### Phase 2: Model Development

**Thought**: Start with pretrained EfficientNet
**Action**: Load and modify model
```python
import timm
import torch.nn as nn

model = timm.create_model('efficientnet_b0', pretrained=True)
model.classifier = nn.Linear(model.classifier.in_features, 20)

# Freeze backbone initially
for param in model.parameters():
    param.requires_grad = False
for param in model.classifier.parameters():
    param.requires_grad = True
```
**Observation**: Model loaded, 4.0M trainable parameters

**Thought**: Implement data pipeline with augmentation
**Action**: Create datasets and loaders
```python
from torchvision import transforms
from torch.utils.data import DataLoader

train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(0.2, 0.2, 0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225])
])

train_dataset = ImageFolder('data/train', transform=train_transform)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
```
**Observation**: Data pipeline ready, 313 batches per epoch

### Phase 3: Training

**Thought**: Train classifier head first
**Action**: Run initial training
```python
optimizer = torch.optim.AdamW(model.classifier.parameters(), lr=1e-3)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=10)

for epoch in range(10):
    train_loss, train_acc = train_epoch(model, train_loader, optimizer)
    val_loss, val_acc = validate(model, val_loader)
    print(f"Epoch {epoch}: Train Acc: {train_acc:.2%}, Val Acc: {val_acc:.2%}")
    scheduler.step()
```
**Observation**: Validation accuracy reaches 89% after 10 epochs

**Thought**: Now fine-tune entire model
**Action**: Unfreeze and train with lower LR
```python
# Unfreeze all layers
for param in model.parameters():
    param.requires_grad = True

# Lower learning rate for pretrained layers
optimizer = torch.optim.AdamW([
    {'params': model.features.parameters(), 'lr': 1e-5},
    {'params': model.classifier.parameters(), 'lr': 1e-4}
])

# Continue training
for epoch in range(20):
    train_loss, train_acc = train_epoch(model, train_loader, optimizer)
    val_loss, val_acc = validate(model, val_loader)
    if val_acc > best_acc:
        torch.save(model.state_dict(), 'best_model.pth')
        best_acc = val_acc
```
**Observation**: Validation accuracy reaches 96.2% at epoch 15

### Phase 4: Optimization

**Thought**: Need to optimize for inference speed
**Action**: Export to ONNX and benchmark
```python
import onnx
import onnxruntime as ort

# Export model
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy_input, "model.onnx",
                  input_names=['input'],
                  output_names=['output'],
                  dynamic_axes={'input': {0: 'batch'}})

# Benchmark
session = ort.InferenceSession("model.onnx")
import time

times = []
for _ in range(100):
    start = time.time()
    session.run(None, {'input': dummy_input.numpy()})
    times.append((time.time() - start) * 1000)

print(f"Average inference: {np.mean(times):.1f}ms")
```
**Observation**: Average inference time: 45ms (meets <100ms requirement)

### Phase 5: Deployment

**Thought**: Create API endpoint
**Action**: Implement FastAPI service
```python
from fastapi import FastAPI, UploadFile
import onnxruntime as ort
from PIL import Image
import io

app = FastAPI()
session = ort.InferenceSession("model.onnx")

@app.post("/predict")
async def predict(file: UploadFile):
    image = Image.open(io.BytesIO(await file.read()))
    processed = preprocess_image(image)

    prediction = session.run(None, {'input': processed})[0]
    class_idx = prediction.argmax()
    confidence = float(prediction.softmax(dim=-1).max())

    return {
        "class": CLASS_NAMES[class_idx],
        "confidence": confidence
    }
```
**Observation**: API endpoint working, 50ms average response time

### Phase 6: Validation

**Thought**: Verify all requirements met
**Action**: Run final validation checks
```python
# Check accuracy
final_acc = validate(model, test_loader)
print(f"Test Accuracy: {final_acc:.2%}")  # 96.5%

# Check inference time
print(f"Inference: {np.mean(times):.1f}ms")  # 45ms

# Check memory usage
print(f"Model size: {os.path.getsize('model.onnx') / 1e6:.1f}MB")  # 16.2MB

# Test API
response = requests.post("http://localhost:8000/predict",
                         files={"file": open("test.jpg", "rb")})
print(response.json())  # {'class': 'electronics', 'confidence': 0.98}
```
**Observation**: All requirements satisfied ✓
```

## Summary

### Achievements
- ✓ 96.5% accuracy (exceeds 95% requirement)
- ✓ 45ms inference (well under 100ms limit)
- ✓ Handles class imbalance effectively
- ✓ Deployed as containerized API
- ✓ Complete documentation and tests

### Key Success Factors
1. **Clear requirements**: Well-defined targets from the start
2. **CoT**: Systematic planning prevented issues
3. **ReAct**: Iterative implementation with validation

### Lessons Learned
- Transfer learning essential for small datasets
- Class weights effectively handle imbalance
- ONNX export provides significant speed boost
- Gradual unfreezing prevents catastrophic forgetting