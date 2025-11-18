# InfoCycle ♻️
## An AI Recycle Classifier

InfoCycle is an AI-powered tool that identifies waste materials (plastic, glass, paper, metal, etc.) from an image and explains whether the item can be recycled. The latest version ships as a simple FastAPI web app so you can drag in a photo and instantly see the classification.

## Setup
1. Clone the repo and enter the folder:  
   `git clone https://github.com/razeenrahman/InfoCycle.git && cd InfoCycle`
2. Create and activate a virtual environment:  
   `python -m venv .venv && source .venv/bin/activate`
3. Install the dependencies:  
   `pip install -r requirements.txt`
4. Launch the FastAPI server:  
   `uvicorn src.app:app --reload`
5. Visit <http://127.0.0.1:8000>, upload an image, and the page will refresh with the predicted class.

## Features
- Upload images via the FastAPI-powered web form and get instant predictions
- Determine recyclability directly from the detected class with helpful emoji labels
- Fast and lightweight inference powered by a fine-tuned ResNet-18 checkpoint

## Current Progress
- Environment setup with GPU-accelerated PyTorch
- Successfully trained a ResNet-18 classification model with PyTorch
- Achieved **97% test accuracy** on the Garbage Classification dataset
- Added model saving + versioned model weights
- Deployed a simple FastAPI web app to upload images and receive classifications

## Future Plans
- Improve the front-end experience (drag-and-drop, responsive layout)
- Display recyclability confidence scores and class probability breakdowns
- Deploy the web app to a managed host so others can try it without setup

## Project Structure
```
InfoCycle/
    model/
        └── infocycle_v1.pth        # trained model weights
    notebooks/
        └── train_model.ipynb       # training + experimentation notebook
    src/
        ├── app.py                  # FastAPI routes + inference logic
        ├── index.html              # upload UI template
        ├── style.css               # styling for the demo site
        ├── model_loader.py         # model + transform loader
        └── utils.py                # recyclability + subcategory helpers
```
