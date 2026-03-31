# GitHub Secrets Configuration for Cloud Run Deployment

Para fazer deploy no Cloud Run, adicione os seguintes secrets no GitHub:

## Environment: `development`

### Required Secrets:

1. **GCP_PROJECT_ID**
   - Seu Google Cloud Project ID
   - Exemplo: `my-project-123456`

2. **GCP_SA_KEY**
   - Chave JSON do Service Account do Google Cloud
   - Como obter:
     1. Acesse Google Cloud Console
     2. Vá para IAM & Admin > Service Accounts
     3. Crie um novo Service Account ou use um existente
     4. Adicione as roles necessárias:
        - Cloud Run Admin
        - Service Account User
        - Cloud Build Service Account
        - Artifact Registry Administrator (se usar Artifact Registry)
     5. Crie uma chave JSON
     6. Copie o conteúdo inteiro do arquivo JSON

3. **GCP_REGION**
   - Região onde o Cloud Run será deployado
   - Exemplos: `us-central1`, `europe-west1`, `asia-northeast1`

4. **CLOUD_RUN_SERVICE_NAME**
   - Nome do serviço no Cloud Run
   - Exemplo: `health-api-dev`

### Optional Environment Variables:

Você também pode adicionar como secrets no environment "development":

5. **DATABASE_URL** (se necessário)
   - Connection string do banco de dados
   - Exemplo: `postgresql://user:password@host:5432/dbname`

6. **ENVIRONMENT**
   - Vai de `development` automaticamente no workflow, mas pode personalizar

## Como adicionar secrets no GitHub:

1. Vá para Settings > Environments > development
2. Clique em "Add secret"
3. Adicione cada secret com seu valor

## Teste de autenticação:

Para testar se tudo está configurado corretamente:

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud run services list
```

## Referências:

- [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
- [GitHub Actions - Google Cloud Auth](https://github.com/google-github-actions/auth)
- [Cloud Run Deploy Action](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service#deploying_the_service)
