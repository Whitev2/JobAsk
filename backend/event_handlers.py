from typing import Callable

from fastapi import FastAPI

from database.postgres import Postgres

event = FastAPI


def start_app_handler(app: FastAPI) -> Callable:
    async def startup() -> None:
        pg = Postgres()
        await pg.connect_to_storage()
        print("Running app start handler.")

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        print("Running app shutdown handler.")

    return shutdown
