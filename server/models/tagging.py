import base64
from typing import Optional

from pydantic import BaseModel, Field


class TaggingRequest(BaseModel):
    base64_image: Optional[str] = Field(None, title="Image", description="Image to classify")

    class Config:
         schema_extra = {
                "example" : {
                    "base64_image" : "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTEhMVFhUXGBgYGBcXFxgYGBcYFxgYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcYGBcY"
                }
            }

class TaggingResponse(BaseModel):
    class Config:
        schema_extra = {
            "example" : {
                "prediction" : "valid"
            }
        }
    prediction: Optional[str] = Field(None, title="Prediction", description="Prediction of the image")

