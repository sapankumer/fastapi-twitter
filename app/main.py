from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.db.base import Base
from app.db.session import engine
from app.routers import auth, comments, likes
from app.routers import users
from app.routers import tweets

# DB create
Base.metadata.create_all(bind=engine)

# App init
app = FastAPI(title="Twitter Clone with JWT Auth")

# Router include
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tweets.router)
app.include_router(comments.router)
app.include_router(likes.router)


# Custom OpenAPI for Bearer Auth
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Twitter Clone",
        version="1.0.0",
        description="API for Twitter Clone with JWT Auth",
        routes=app.routes,
    )

    # Bearer token security scheme
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "Bearer",
            "bearerFormat": "JWT",
        }
    }
    # openapi_schema["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# Override default OpenAPI
app.openapi = custom_openapi
