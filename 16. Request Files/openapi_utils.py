from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema

    schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
    )

    components = schema.get("components", {}).get("schemas", {})

    for component in components.values():
        for prop in component.get("properties", {}).values():
            items = prop.get("items", {})

            if items.get("contentMediaType") == "application/octet-stream":
                items.pop("contentMediaType")
                items["format"] = "binary"

    app.openapi_schema = schema
    return schema