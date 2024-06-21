from ultralytics import YOLO

# Load a model
model = YOLO("model_files/gender_segment1.pt")  # To load the custom model file

# Predict with the model
results = model("web_scrapped_image_data/gender/males/half_sleeves/")  # predict on the images
