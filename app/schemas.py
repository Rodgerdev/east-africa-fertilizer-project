from pydantic import BaseModel

class CropInput(BaseModel):
    fertilizer: float
    cereal_yield: float
    arable_land: float
