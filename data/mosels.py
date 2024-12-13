from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import BigInteger, String, ForeignKey
engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3")

async_session = async_sessionmaker(engine)

class Base(DeclarativeBase, AsyncAttrs):
    pass


class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    subscribe: Mapped[str] = mapped_column(String(10))
    datesubscribe: Mapped[str] = mapped_column(String(10))

class Profi(Base):
    __tablename__ = "Profies"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("Users.user_id"))
    user_name: Mapped[str] = mapped_column(String(100))
    full_name: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(15))
    chat_city: Mapped[str] = mapped_column(String(25))
    self_cat: Mapped[str] = mapped_column(String(25))
    self_subcat: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(15))
    promo_link: Mapped[str] = mapped_column(String(255))
    price: Mapped[str] = mapped_column(String(100))

async def async_main():
    async with engine.begin() as db:
        await db.run_sync(Base.metadata.create_all)




