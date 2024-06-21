from ultralytics import YOLO

# Load a model
model = YOLO("model_files/sleeves2.pt")  # To load the custom model file

# Predict with the model
results = model("web_scrapped_image_data/gender/females/full_sleeves/")  # predict on the images
