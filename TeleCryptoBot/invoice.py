from pydantic import BaseModel

from typing import Union, Optional, List
from datetime import datetime

from .base import Assets, PaidButtons, InvoiceStatus, CurrencyType


class Invoice(BaseModel):
    invoice_id: int
    status: Union[InvoiceStatus, str]
    hash: str
    asset: Optional[Union[Assets, str]] = None
    amount: Union[int, float]
    bot_invoice_url: str
    description: Optional[str] = None
    created_at: datetime
    allow_comments: bool
    allow_anonymous: bool
    expiration_date: Optional[str] = None
    paid_at: Optional[datetime] = None
    paid_anonymously: Optional[bool] = None
    comment: Optional[str] = None
    hidden_message: Optional[str] = None
    payload: Optional[str] = None
    paid_btn_name: Optional[Union[PaidButtons, str]] = None
    paid_btn_url: Optional[str] = None
    currency_type: Union[CurrencyType, str]
    fiat: Optional[str] = None
    paid_asset: Optional[Union[Assets, str]] = None
    paid_amount: Optional[Union[int, float]] = None
    paid_usd_rate: Optional[Union[int, float]] = None
    fee_asset: Optional[Union[Assets, str]] = None
    fee_amount: Optional[Union[int, float]] = None
    accepted_assets: Optional[Union[List[Union[Assets, str]], str]] = None