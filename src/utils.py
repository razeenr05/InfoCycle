# quick lookup tables
RECYCLABLE = {
    "brown-glass": True,
    "green-glass": True,
    "white-glass": True,
    "paper": True,
    "plastic": True,
    "metal": True,
    "cardboard": True
}

NON_RECYCLABLE = {
    "battery": False,
    "biological": False,
    "trash": False,
    "shoes": False,
    "clothes": False
}

def classify_recyclability(label):
    # decision
    if label in RECYCLABLE:
        return "Recyclable ♻️", True
    else:
        return "Not Recyclable ❌", False

def get_subcategory(label):
    # surface a friendly category name for the ui
    if "glass" in label:
        return "Glass → " + label
    if label in ["clothes", "shoes"]:
        return "Apparel → " + label
    return label
