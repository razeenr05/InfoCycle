from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from .model_loader import load_model, transform, CLASS_NAMES
from .utils import classify_recyclability, get_subcategory
from PIL import Image
import torch
import io
import os

# device selection
device = (
    "cuda" if torch.cuda.is_available() 
    else
    "mps" if torch.backends.mps.is_available() 
    else
    "cpu"
)

# load the trained classifier once so later requests stay fast
model = load_model(device=device)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def serve_home():
    with open("src/index.html", "r") as f:
        content = f.read()
    return content.replace("{{result}}", "")

@app.get("/style.css")
def serve_css():
    return FileResponse("src/style.css")


@app.post("/predict", response_class=HTMLResponse)
async def predict(file: UploadFile = File(...)):

    # read the upload and convert to tensor expected by the model
    img_bytes = await file.read()
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")

    img_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = torch.max(outputs, 1)
        label = CLASS_NAMES[predicted.item()]

    recyclable_text, _ = classify_recyclability(label)
    subcategory_text = get_subcategory(label)

    # render a small html fragment that will replace the placeholder
    result_html = f"""
        <h2>Prediction: {label}</h2>
        <p><b>{recyclable_text}</b></p>
        <p>Subcategory: {subcategory_text}</p>
    """

    with open("src/index.html", "r") as f:
        page = f.read()

    # swap the template marker with the latest prediction
    return page.replace("{{result}}", result_html)
