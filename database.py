import psycopg2

import settings


def get_message_text_from_db(message_type: str) -> str:
    with psycopg2.connect(dbname=settings.DB_NAME,
                          host=settings.DB_HOST,
                          port=settings.DB_PORT,
                          user=settings.POSTGRES_USER,
                          password=settings.POSTGRES_PASSWORD) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT content FROM messages WHERE message_type = %s",
                (message_type,)
            )
            result = cur.fetchone()
            return result[0] if result else ''
