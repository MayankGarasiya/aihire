## EC2 deployment (Dockerized Django + Nginx + Gunicorn)

### Architecture

- EC2 instance runs Docker + Docker Compose
- Containers:
  - `backend` (Gunicorn)
  - `nginx` (reverse proxy)
  - `celery_worker`, `celery_beat`
  - `rabbitmq`

### Steps (high level)

1. Provision EC2 (Ubuntu) + Security Group:
   - Allow inbound 80/443 from internet
   - Allow inbound 22 from your IP
2. Install Docker + Docker Compose plugin.
3. Copy repository to EC2 (git clone).
4. Create `backend/.env` from `backend/.env.example` (use prod values).
5. Bring up services:

```bash
docker compose -f docker-compose.prod.yml up -d --build
```

6. Point your domain to the EC2 public IP.
7. Add TLS (recommended):
   - Use Certbot on host, or a managed ALB in front, or Nginx + certbot container.

### Operational notes

- Put secrets in SSM Parameter Store or Secrets Manager (preferred) and inject them at deploy time.
- Use CloudWatch agent / centralized logging.
- Consider moving RabbitMQ to Amazon MQ for managed ops.

