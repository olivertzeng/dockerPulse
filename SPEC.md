## Project Goal
Docker dashboard and watchdog. `/var/run/docker.sock` monitors and control containers directly. Uses FastAPI(backend) + (Svelte + TailwindCSS(frontend))

# Barebones
- [ ] Connect to `/var/run/docker.sock` w `docker` module.
- [ ] GET `/api/containers`: Return a JSON list of all containers (ID, Name, Status, Image).
- [ ] GET `/api/stats/{container_id}`: Return real-time CPU/RAM usage for a specific container.
- [ ] POST `/api/containers/{container_id}/action`: Accept an action like `start`, `stop`, or `restart` and execute it.
- [ ] Error handling

---

# UI

- [ ] Global Layout:
  - [ ] Dark mode by default
  - [ ] Navigation Bar
  - [ ] Dark/Light autoswitch
- [ ] Main Dashboard:
  - [ ] Choose layout(proceed AFTER "Barebones" grid/list/both etc...)

---

## Docker

- [ ] `Dockerfile`
- [ ] `docker-compose.yml`
- [ ] Upload to dockerhub

---

### Niche

- [ ] username passwd auth
- [ ] Auto-Rescue Watchdog
- [ ] Log inspection
- [ ] Batch Actions: Selectable entries for each service
- [ ] `docker pull` cronjob
- [ ] Docker CLI wrapper
