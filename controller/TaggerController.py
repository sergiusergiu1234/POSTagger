

from typing import Annotated
from fastapi import APIRouter, Depends, Query, Security

from service.TaggerService import TaggerService


router = APIRouter(tags=['POS Tagger'])

@router.post('/tag')
async def tag(text: Annotated[str, Query(...)] = None):
    resp = TaggerService.tag(text=text)
    return {"response": resp}