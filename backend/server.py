from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import config
from event_handlers import start_app_handler, stop_app_handler
from news import router as news_router


def get_app() -> FastAPI:
    print("🚀🚀🚀 Starting server..")
    fast_app = FastAPI()

    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )

    # fast_app.include_router(health.ping)
    fast_app.include_router(news_router.router, prefix="/news")

    #
    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))

    print("Server is started")
    return fast_app


app = get_app()
