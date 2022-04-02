from unittest import result
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.models.classify import *
import pandas as pd
from server.ml.classify import *
from server.models.reponse import *



router = APIRouter()
mobile_net = Classify('./server/ml/saved/train.h5')


@router.post("/", response_description="Check valid Image")
async def check_valid_image(request: ClassifyRequest):
    data = jsonable_encoder(request)
    
    print(data)

    base64_image = data['base64_image']

    result = mobile_net.predict(base64_image)
    
    response = {
        "result" : result,
    }
    return Response.ResponseModel(response, "Success")
