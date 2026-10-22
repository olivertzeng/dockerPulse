import docker
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = docker.from_env()

@app.get("/")
def get_all_containers():
    containers = client.containers.list(all=True)

    result = []
    for c in containers:
        result.append({"name": c.name, "status": c.status})

    return result
