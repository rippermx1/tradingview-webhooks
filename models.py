from pydantic import BaseModel

''' Alert Template 
{
    "side": "BUY",
    "exchange": "{{exchange}}",
    "symbol": "{{ticker}}",
    "price": "{{close}}"
} 
'''
class Alert(BaseModel):
    side: str
    exchange: str
    symbol: str
    price: str