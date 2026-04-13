## AWS Amplify deployment (Next.js)

### Prereqs

- A GitHub repo with this monorepo pushed
- Amplify Console access

### Steps

1. In AWS Amplify Console, choose **New app → Host web app**.
2. Connect GitHub and select the repository + branch.
3. Set **App root** to `frontend`.
4. Build settings:
   - Amplify will detect Next.js. If prompted, use:

```yaml
version: 1
applications:
  - appRoot: frontend
    frontend:
      phases:
        preBuild:
          commands:
            - npm ci
        build:
          commands:
            - npm run build
      artifacts:
        baseDirectory: .next
        files:
          - '**/*'
      cache:
        paths:
          - node_modules/**/*
```

5. Add environment variables (Amplify → App settings → Environment variables):
   - `NEXT_PUBLIC_API_BASE_URL` (e.g. `https://api.yourdomain.com/api`)
6. Deploy.

### Notes

- Use a custom domain and point it at Amplify.
- Ensure your backend CORS allows the Amplify domain.

