## AIHire — AI-powered interview platform

Monorepo:

- `backend/`: Django REST Framework + SimpleJWT + Celery (RabbitMQ) + S3
- `frontend/`: Next.js (App Router) + TypeScript + Tailwind CSS

### Quick start (local)

Prereqs: Docker, Docker Compose.

1. Create env files:
   - `backend/.env` from `backend/.env.example`
   - `frontend/.env.local` from `frontend/.env.example`
2. Start services:

```bash
docker compose up --build
```

3. Backend:
   - API: `http://localhost:8000/api/`
   - Admin: `http://localhost:8000/admin/`

4. Frontend:
   - App: `http://localhost:3000/`

### Deploy

- Frontend: AWS Amplify (see `docs/amplify.md`)
- Backend: Dockerized Django on EC2 with Nginx + Gunicorn (see `docs/ec2-backend.md`)

