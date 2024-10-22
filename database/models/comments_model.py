from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import BigInteger


class Base(DeclarativeBase):
    pass


class AbstractModel(AsyncAttrs, Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class CommentsModel(AbstractModel):
    user_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column()
    comment: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Comment(id={self.id!r}, user_id={self.user_id!r}, username={self.username!r}, comment={self.comment!r})"
