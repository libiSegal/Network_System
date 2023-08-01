from fastapi import APIRouter, Form,Depends
from moduls import technician_crud
from moduls import security
technician_router = APIRouter()


@technician_router.get('/{technician_id}')
async def get_technician_details(technician_id,current_user: security.User = Depends(security.get_current_active_user)):
    return technician_crud.get_technician_details(technician_id)

