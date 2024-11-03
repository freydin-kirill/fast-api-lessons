import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=550, detail={
            "status": "success",
            "data": None,
            "details": repr(e)
        })


@router.post("/")
async def add_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    statement = insert(operation).values(**new_operation.dict())
    await session.execute(statement)
    await session.commit()  # завершить и исполнить транзакцию
    return {"status": "success"}


@router.get("/long_operation")
@cache(expire=30)
async def get_long_operation():
    time.sleep(3)
    return {"status": "Too long!"}

