from fastapi import APIRouter, Query, Depends
from src.schemas import GetWalletInfoResponse, GetWalletInfoRequest, GetWalletQueriesResponse
from src.tron_client import TronClient
from src.db.repositories import WalletQueryRepository

router = APIRouter(prefix='/wallet', tags=['wallet'])


@router.post("/info", response_model=GetWalletInfoResponse)
async def get_wallet_info(
        data: GetWalletInfoRequest,
        tron_client: TronClient = Depends(TronClient),
        wallet_query_repository: WalletQueryRepository = Depends(WalletQueryRepository)
):
    wallet_info = await tron_client.get_wallet_info(address=data.address)
    await wallet_query_repository.save_wallet_query(**wallet_info)
    return wallet_info


@router.get("/queries", response_model=GetWalletQueriesResponse)
async def get_wallet_queries(
        page: int = Query(1, ge=1),
        per_page: int = Query(10, ge=1, le=100),
        wallet_query_repository: WalletQueryRepository = Depends(WalletQueryRepository)
):
    response = await wallet_query_repository.get_queries(page, per_page)
    return response
