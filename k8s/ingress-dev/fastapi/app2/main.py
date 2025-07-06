from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

class EchoBody(BaseModel):
    message: str

@app.post("/echo")
def echo(body: EchoBody):
    return {"you_said": body.message}

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>FastAPI Test App</title>
        </head>
        <body>
            <h1>🚀 FastAPI 2 앱이 정상적으로 실행 중입니다!</h1>
            <p>이 페이지는 Kubernetes에 배포된 테스트용 FastAPI 앱입니다.</p>
            <p><a href="/health">[헬스 체크]</a></p>
            <p><a href="/docs">[Swagger UI 보기]</a></p>
        </body>
    </html>
    """