import docker
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()

client = docker.from_env()

@app.get("/api/containers")
def get_all_containers():
    containers = client.containers.list(all=True)

    result = []
    for c in containers:
        result.append({"name": c.name, "status": c.status})

    return result

app.mount("/api/containers", StaticFiles(directory="static", html=True), name="static")
