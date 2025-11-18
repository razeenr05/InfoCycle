import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

CLASS_NAMES = [
    'battery', 'biological', 'brown-glass', 'cardboard', 'clothes',
    'green-glass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'white-glass'
]

# compact label list mirrors the order used during training
def load_model(model_path="model/infocycle_v1.pth", device="cpu"):
    model = models.resnet18(weights=None)
    num_features = model.fc.in_features
    # swap the final layer so resnet outputs our class count
    model.fc = nn.Linear(num_features, len(CLASS_NAMES))

    state_dict = torch.load(model_path, map_location=device)
    model.load_state_dict(state_dict)

    model.to(device)
    model.eval()
    return model

# basic resizing and tensor conversion for uploaded images
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])
