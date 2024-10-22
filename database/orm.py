from sqlalchemy import select

from database.db import DatabaseSessionManager
from database.models.comments_model import CommentsModel

from typing import List, Sequence


class ORMManager(DatabaseSessionManager):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_table(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(CommentsModel.metadata.drop_all)
            await connection.run_sync(CommentsModel.metadata.create_all)

    async def create_comment(
            self, user_id: int, username: str, comment: str
    ) -> CommentsModel:
        async with self.session() as session:
            comment = CommentsModel(
                user_id=user_id,
                username=username,
                comment=comment
            )
            session.add(comment)
            await session.commit()
            await session.refresh(comment)
        return comment

    async def get_comment(self, user_id: int) -> CommentsModel:
        async with self.session() as session:
            comment = await session.execute(
                select(CommentsModel).where(CommentsModel.user_id == user_id)
            )
            if comment:
                return comment.scalars().one()
            else:
                raise Exception("Comment not found")

    async def get_comments(self) -> Sequence[CommentsModel]:
        async with self.session() as session:
            comments = await session.execute(
                select(CommentsModel)
            )
            return comments.scalars().all()

    async def clear_table(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(CommentsModel.metadata.drop_all)
            await connection.run_sync(CommentsModel.metadata.create_all)


orm_manager = ORMManager()
