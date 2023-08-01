from fastapi import APIRouter, Form
from moduls import technician_crud

technician_router = APIRouter()


@technician_router.get('/{technician_id}')
async def get_technician_details(technician_id):
    return technician_crud.get_technician_details(technician_id)

