from asyncio import sleep
from fastapi import FastAPI
from starlette.responses import PlainTextResponse


fastapi_app = FastAPI()


@fastapi_app.get("/delay")
async def delay():
    await sleep(0.3)
    return PlainTextResponse("ok")


@fastapi_app.get("/simple")
def simple():
    return PlainTextResponse("ok")
