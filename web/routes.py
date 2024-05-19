from fastapi import APIRouter # type: ignore

router = APIRouter()

@router.get("/test")
async def test():
    return "Hello VS Code API World!"