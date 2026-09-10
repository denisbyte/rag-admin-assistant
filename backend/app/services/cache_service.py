"""
 Service de cache Redis
"""

import hashlib
import json

from backend.app.infrastructure.redis_client import get_redis_client

CACHE_TTL = 3600

def _build_cache_key(question: str) -> str:
    normalized_question  = question.strip().lower()

    question_hash = hashlib.sha256(
        normalized_question.encode("utf-8")
    ).hexdigest()

    return f"rag:chat:{question_hash}"

def get_cached_response(question:str) -> dict | None:
    # Recupère une réponse Redis si elle existe
    redis_client = get_redis_client()
    cache_key = _build_cache_key(question)

    cached_data = redis_client.get(cache_key)
    if cached_data is None:
        return None
    return json.loads(cached_data)

def set_cached_response(question: str, data: dict) -> None:
    # Enregistrer une réponse dans Redis avec un TTL
    redis_client = get_redis_client()
    cache_key = _build_cache_key(question)

    redis_client.setex(
        cache_key,
        CACHE_TTL,
        json.dumps(data, ensure_ascii=False)
    )


