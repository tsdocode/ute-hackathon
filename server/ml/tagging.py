import base64
import binascii
import io
import os
from google.cloud import vision
from typing import List



class Tagging():
    def __init__(self) -> None:
        self.client = vision.ImageAnnotatorClient()

    def predict(self, base64_image: str) -> List[str]:
        content = binascii.a2b_base64(base64_image)
        image = vision.Image(content=content)

        response = self.client.label_detection(image=image)
        labels = response.label_annotations
        
        result = [label.description for label in labels]

        return result


