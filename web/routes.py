from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test():
    return "Hello VS Code API World!"