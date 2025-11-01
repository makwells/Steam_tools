import aiosqlite

from typing import Optional
import sys

from loguru import logger

from config import DB_NAME

conn: Optional[aiosqlite.Connection] = None

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>"
)
async def init_db(DB_FILE: str) -> None:
    global conn
    conn = await aiosqlite.connect(DB_FILE)

    await conn.execute("""
        CREATE TABLE IF NOT EXISTS wishlists (
            id INTEGER PRIMARY KEY,
            game_name TEXT NOT NULL,
            game_type TEXT NOT NULL,
            app_id BIGINT NOT NULL,
            price INTEGER NOT NULL,
            discount_price INT NULL
        )
""")
    await conn.commit()
    logger.info("Database {} inited.", DB_FILE)

async def add_game(game_name: str, game_type: str, app_id: int, price: int, discount_price: int = None):
    await conn.execute(
        "INSERT INTO wishlists (game_name, game_type, app_id, price, discount_price) VALUES (?, ?, ?, ?, ?)",
        (game_name, game_type, app_id, price, discount_price if discount_price else "")
    )
    await conn.commit()
    logger.info(f"Succefully added {game_name} w {price} price and {discount_price} like discount price. APP_ID is {app_id}")

async def game_exists(game_name: str) -> bool:
    cursor = await conn.execute(
        "SELECT 1 FROM wishlists WHERE game_name = ? LIMIT 1",
        (game_name,)
    )
    result = await cursor.fetchone()
    await cursor.close()
    return result is not None

async def delete_game(game_name: str):
    exist = await game_exists(game_name=game_name)
    if not exist:
        logger.error(f"Game {game_name} not exist in database")
        return
    
    cursor = await conn.execute(
        "DELETE FROM wishlists WHERE game_name = ?",
        (game_name,)
    )
    await conn.commit()
    
    rows_affected = cursor.rowcount
    if rows_affected > 0:
        logger.info(f"Successfully deleted game '{game_name}' from wishlist")
        return True
    else:
        logger.warning(f"Game '{game_name}' not found in wishlist")
        return False