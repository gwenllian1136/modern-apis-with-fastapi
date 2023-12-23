import fastapi
from typing import Optional

from fastapi import Depends
from pydantic import BaseModel
from models.Location import Location
from services import openweather_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(loc:Location = Depends(), units: Optional[str] = 'metric'):

#    return f"City is {loc.city},State is {loc.state}, Country is {loc.country} and units ={units}"
    report = await openweather_service.get_report_async(loc.city, loc.state, loc.country, units)
    return report
