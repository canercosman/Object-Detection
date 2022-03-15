import os, io
from google.cloud import vision
from Pillow_Utility import draw_borders, Image, drawVertices

#Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of the JSON file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'PrivateKey.json'
client = vision.ImageAnnotatorClient()

FILE_NAME = "image.jpg"
IMAGE_PATH = os.path.join("\\relative\\path", FILE_NAME)

with io.open(IMAGE_PATH, 'rb') as image_file:
     content = image_file.read()

image = vision.types.Image(content=content)
response = client.object_localization(image=image)
localized_object_annotations = response.localized_object_annotations

pillow_image = Image.open(IMAGE_PATH)

evidences = {"Laptop":1, "Mobile phone":2, "Printer":3, "Computer monitor":4}

for obj in localized_object_annotations:
    if format(obj.name) in evidences:
        
        if format(obj.name)=='Laptop':
         evidence_id="1.1"
        elif format(obj.name)=='Mobile phone':
         evidence_id="2.1"
        elif format(obj.name)=='Printer':
         evidence_id="3.1"
        elif format(obj.name)=='Computer monitor':
         evidence_id="4.1"            
     
        r, g, b = 255, 255, 255
     
        draw_borders(pillow_image, obj.bounding_poly, (r, g, b),
                     pillow_image.size, obj.name, evidence_id)
    
pillow_image.show()