import DAL


async def get_all_news():
    query = DAL.news.select()
    return await DAL.database.fetch_all(query)

async def get_news_by_id(news_id: int):
    query = DAL.news.select().where(DAL.news.c.id == news_id)
    return await DAL.database.fetch_one(query)
