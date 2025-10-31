## ♻️ InfoCycle — AI Recycle Classifier

An AI-powered tool that identifies and classifies waste materials such as **plastic, glass, paper, and metal** using image recognition.  
The goal of **InfoCycle** is to help users determine whether an item is recyclable with just a single image.

In the future, InfoCycle will (hopefully) be available as a **simple web app** where users can upload a photo and instantly receive a classification result.  
If not deployed as a web app, it will include a **standalone Python script (`predict.py`)** that takes an image file and outputs the detected material type and recyclability!

## Features (Planned)
- Classify uploaded images into material categories (plastic, paper, glass, metal, etc.)  
- Determine recyclability directly from an image  
- Fast and lightweight inference with a pre-trained model  
- Option to run locally using `predict.py`  
- Future web integration with an upload based UI  
- Powered by a ResNet-18 deep learning model trained in **PyTorch**

## Current Progress
- Project structure created and organized  
- Environment setup with GPU enabled PyTorch (for me only)
- (WIP) Developing and training the ResNet-18 model (`train_model.ipynb`)  

## Future Plans
- Complete model training and release downloadable model
- Add `predict.py` for quick local image testing 
- Display recyclability confidence score and category breakdown  
- Develop and deploy web app

## Project Structure
InfoCycle/  
    model/                Trained model weights (to be added)  
    notebooks/            Model training and experimentation  
        ── train_model.ipynb  
    src/                  Future: predict.py and web app scripts  