from fastapi import FastAPI

from controller import TaggerController


app = FastAPI( title="BusinessAnalystServiceAPI")

app.include_router(TaggerController.router)