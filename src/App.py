from fastapi import FastAPI
import router.DefaultRouter as DefaultRouter

app = FastAPI()

app.include_router(DefaultRouter.router)


