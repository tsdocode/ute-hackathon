from unittest import result
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.models.simmilarly import *
import pandas as pd
from server.ml.simmilarly import *
from server.ml.tagging import *
from server.models.reponse import *
import requests




router = APIRouter()

sim_model = Simmilarly()
gcp_tagging = Tagging()



def get_all_room():
    url = "https://api-troviet.herokuapp.com/api/all-rooms"
    response = requests.get(url)
    return response.json()



@router.post("/", response_description="Check valid Image")
async def check_valid_image(request: SimRequest):
    data = jsonable_encoder(request)
    user_image = data['user_image']
    
    all_room = get_all_room()


    user_tags = []

    for image in user_image:
        user_tags.extend(gcp_tagging.predict(image))

    user_tags = list(set(user_tags))


    for room in all_room:
        room['corr'] = sim_model.predict(" ".join(user_tags), "".join(room['keyword']))


    all_room = sorted(all_room, key=lambda d: d['corr'], reverse=True)


    return all_room



    
