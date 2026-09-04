"""
    MULTIPLE MIDDLEWARE EXECUTION ORDER
    - You can add multiple middlewares using either @app.middleware() decorator or app.add_middleware() method.
    - Each new middleware wraps the application, forming a stack.
    - The last middleware added is the outermost, and the first is the innermost.
    - On the request path, the outermost middleware runs first.
    - On the response path, it runs last.
    - For example:
            app.add_middleware(MiddlewareA)
            app.add_middleware(MiddlewareB)
    - This results in the following execution order:  
        * Request: MiddlewareB → MiddlewareA → route
        * Response: route → MiddlewareA → MiddlewareB
"""


from fastapi import FastAPI, Request 

app = FastAPI()

@app.middleware('http')
async def middleware_a(request: Request, call_next):
    print("➡️ Middleware A - Request")
    response = await call_next(request)
    print("➡️ Middleware A - Response")
    return response

@app.middleware('http')
async def middleware_b(request: Request, call_next):
    print("➡️ Middleware B - Request")
    resposne = await call_next(request)
    print("➡️ Middleware B - Response")
    return resposne

@app.get('/')
async def home():
    print("🏠 Route")
    return {'message': 'Hello World!'}