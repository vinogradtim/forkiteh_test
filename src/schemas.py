from _decimal import Decimal

from pydantic import BaseModel, field_validator, ConfigDict


class GetWalletInfoRequest(BaseModel):
    address: str

    @field_validator("address")
    def validate_address(cls, a: str):
        if len(a) != 34 or a[0] != "T":
            raise ValueError('Invalid address')
        return a


class GetWalletInfoResponse(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int


class WalletQuery(GetWalletInfoResponse):
    id: int

    model_config = ConfigDict(from_attributes=True)


class GetWalletQueriesResponse(BaseModel):
    total: int
    page: int
    per_page: int
    pages: int
    queries: list[WalletQuery]
