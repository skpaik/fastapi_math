from typing import List

from pydantic import BaseModel, Field


class NumbersResponse(BaseModel):
    total_sum: int = Field(..., example=20)
    even_sum: int = Field(..., example=6)
    odd_sum: int = Field(..., example=14)
    average: float = Field(..., example=2.857)
    max: int = Field(..., example=5)
    min: int = Field(..., example=1)
    median: float = Field(..., example=3)
    mode: List[int] = Field(..., example=[2, 3])
    std_dev: float = Field(..., example=1.676)
    count: int = Field(..., example=7)

    class Config:
        json_schema_extra = {
            "example": {
                "total_sum": 20,
                "even_sum": 6,
                "odd_sum": 14,
                "average": 2.857,
                "max": 5,
                "min": 1,
                "median": 3,
                "mode": [2, 3],
                "std_dev": 1.676,
                "count": 7,
            }
        }
