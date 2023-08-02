from fastapi import APIRouter, Form, Depends, HTTPException
from moduls import technician_crud
from moduls import security
from log_file import logger

technician_router = APIRouter()


@logger
@technician_router.get('/{technician_id}')
async def get_technician_details(technician_id,
                                 current_user: security.User = Depends(security.get_current_active_user)):
    if not technician_id.isdecimal():
        raise HTTPException(400, 'Invalid input')
    return technician_crud.get_technician_details(technician_id)
