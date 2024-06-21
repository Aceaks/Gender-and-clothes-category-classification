Gender and Sleeve Type Classification using YOLO v8

Welcome to the Gender and Sleeve Type Classification project! This project uses YOLO v8 for image segmentation to classify gender and sleeve types (full sleeves and half sleeves) from web-scraped images. All training data is annotated and models are prepared by me.

Table of Contents
Introduction
Features
Dataset
Installation
Usage
Results
Contributing
Introduction
In this project, we aim to classify images based on gender and the type of sleeves (full sleeves and half sleeves) using the YOLO v8 model. The images used for training the model are web-scraped and manually annotated.

Features
Web-Scraped Data: Images scraped from various sources.
Manual Annotation: All images are manually annotated for accurate training.
YOLO v8: Utilizes the latest YOLO v8 for image segmentation.
Classification: Identifies gender and sleeve type.
Dataset
The dataset for this project is collected from web scraping various sources and manually annotated for gender and sleeve types. The annotation process involved labeling each image with the correct gender and sleeve type.

Installation
To get started, clone the repository and install the required dependencies.

https://github.com/Aceaks/Gender-and-clothes-category-classification.git
cd Gender-and-clothes-category-classification
pip install -r requirements.txt
Usage
To run the model on new images, follow these steps:

Place your images in the respective input directory.
Run the prediction script:
gender_classify.py and sleeves_classify.py

Results
Here are some sample results from the trained model:



Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards.


