import DAL
from sqlalchemy import select, update

async def get_all_news(limit: int = 10, offset: int = 0):
    query = DAL.news.select().limit(limit).offset(offset)
    return await DAL.database.fetch_all(query)

async def get_news_by_category(category_id: int, limit: int, offset: int):
    # Получаем новости, которые соответствуют условиям запроса
    select_query = (
        select(DAL.news)
        .where((DAL.news.c.category_id == category_id) & (DAL.news.c.is_read == False))
        .limit(limit)
        .offset(offset)
    )
    news = await DAL.database.fetch_all(select_query)
    
    # Помечаем выбранные новости как прочитанные
    if news:
        news_ids = [record['id'] for record in news]
        update_query = (
            update(DAL.news)
            .where(DAL.news.c.id.in_(news_ids))
            .values(is_read=True)
        )
        await DAL.database.execute(update_query)

    return news
