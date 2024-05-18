from fastapi import FastAPI
import uvicorn

from web.routes import router as router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5555, reload=True)