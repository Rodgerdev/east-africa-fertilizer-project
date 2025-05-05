from pydantic import BaseModel, Field

class CropInput(BaseModel):
    fertilizer: float = Field(..., example=50.5, description="Fertilizer consumption (kg per hectare)")
    cereal_yield: float = Field(..., example=3000.0, description="Cereal yield (kg per hectare)")
    arable_land: float = Field(..., example=0.5, description="Arable land (hectares per person)")
