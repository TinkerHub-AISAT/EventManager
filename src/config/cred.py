import os

from dotenv import load_dotenv

load_dotenv()


def supabase_url() -> str:
    return os.environ.get("SUPABASE_URL")


def supabase_key() -> str:
    return os.environ.get("SUPABASE_KEY")
