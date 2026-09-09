"""
Client Redis utilisé par l'application pour la gestion du cache
"""
import redis

from backend.app.core.config import settings

def get_redis_client() -> redis.Redis:
    # Retourne un client redis configuré pour l'application
    return redis.from_url(
        settings.redis_url,
        decode_responses=True,
    )
