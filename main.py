import docker
from fastapi import FastAPI

app = FastAPI()

client = docker.from_env()

@app.get("/api/containers")
def get_all_containers():
    containers = client.containers.list(all=True)

    result = []
    for c in containers:
        result.append({"name": c.name, "status": c.status})

    return result
