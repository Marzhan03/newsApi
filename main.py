from fastapi import FastAPI
import asyncio
import DAL, data_accessor
import sys, uvicorn, signal

app = FastAPI()

@app.get("/news/{category_id}/{limit}/{offset}")
async def get_news(category_id: int, limit:int, offset:int):
    await DAL.database.connect()
    result = await data_accessor.get_news_by_category(category_id=1, limit=limit, offset=offset)
    await DAL.database.disconnect()
    return result


def graceful_shutdown(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGTERM, graceful_shutdown)

if __name__ == "__main__":
    uvicorn.run("main:app", host='10.100.1.16', port=8000, reload=True, workers=3)
