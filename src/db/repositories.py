from sqlalchemy import select, func

from src.db.models import WalletQuery
from src.db.base import async_session_maker


class WalletQueryRepository:
    async def save_wallet_query(self, address: str, balance: float, bandwidth: int, energy: int) -> dict:
        async with async_session_maker() as session:
            query = WalletQuery(address=address, balance=balance, bandwidth=bandwidth, energy=energy)
            session.add(query)
            await session.commit()
            await session.refresh(query)
            return {'status': 'saved', 'query': query}

    async def get_queries(self, page: int, per_page: int) -> dict:
        async with async_session_maker() as session:
            total_stmt = select(func.count()).select_from(WalletQuery)
            total = (await session.execute(total_stmt)).scalar()

            stmt = (
                select(WalletQuery)
                .offset((page - 1) * per_page)
                .limit(per_page)
            )
            queries = (await session.execute(stmt)).scalars().all()

            return {
                "total": total,
                "page": page,
                "per_page": per_page,
                "pages": (total + per_page - 1) // per_page,
                "queries": queries
            }
