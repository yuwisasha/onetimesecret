from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"])


async def verify(string: str, hashed_string: str) -> bool:
    return pwd_context.verify(string, hashed_string)


async def get_hash(string: str) -> str:
    return pwd_context.hash(string)
