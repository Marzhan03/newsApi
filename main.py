from fastapi import FastAPI
import asyncio
import DAL, data_accessor

app = FastAPI()

@app.get("/news/{news_id}")
async def get_news(news_id: int):
    await DAL.database.connect()
    result = await data_accessor.get_news_by_id(news_id)
    await DAL.database.disconnect()
    return result
