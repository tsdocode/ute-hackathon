import base64
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

class RoomTagItem(BaseModel):
    room_id: str
    tag: List[str]



class SimRequest(BaseModel):
    user_image: List[str] = Field(None, title="Image", description="Tag from User Image")
    # room_tag: List[RoomTagItem] = Field(None, title="Room Tag", description="Tag from Room")

    class Config:
         schema_extra = {
                "example" : {
                    "user_image" : ["a", "b", "c"],
                    # "room_tag" : [
                    #     {
                    #         "room_id" : "1",
                    #         "tag" : ["a", "b", "c"]
                    #     },
                    #     {
                    #         "room_id" : "2",
                    #         "tag" : ["a", "b", "c"]
                    #     }
                    # ]
                }
            }

class SimResponse(BaseModel):
    class Config:
        schema_extra = {
            "example" : {
                "prediction" : "valid"
            }
        }
    prediction: Optional[str] = Field(None, title="Prediction", description="Prediction of the image")

