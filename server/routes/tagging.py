from unittest import result
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.models.tagging import *
import pandas as pd
from server.ml.tagging import *
from server.models.reponse import *



router = APIRouter()
gcp_tagging = Tagging()


@router.post("/", response_description="Check valid Image")
async def check_valid_image(request: TaggingRequest):
    data = jsonable_encoder(request)
    
    print(data)

    base64_image = data['base64_image_arr']
    result = []

    for image in base64_image:
        result.extend(gcp_tagging.predict(image))
        
    result = gcp_tagging.predict(base64_image)

    return Response.ResponseModel(data=result, message="Success")
