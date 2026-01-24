from functools import lru_cache
import os

from supabase import create_client


@lru_cache(maxsize=1)
def get_supabase_client():
    return create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_KEY"),
    )

