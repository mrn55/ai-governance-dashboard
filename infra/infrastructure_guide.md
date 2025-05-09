# ☁️ Infrastructure Guide for AI Governance Dashboard

This guide outlines how to deploy and manage the infrastructure for the AI Governance Dashboard using PowerShell scripts and GitHub Actions.

---

## 🛠️ Setup Steps

### 1. Deploy Core Azure Resources

Run `1-deploy.ps1` to create:

- Azure Resource Group: `ai-governance-demo`
- Azure Container Registry (ACR)
- Azure Container App Environment
- A placeholder Container App for initial setup

```powershell
.\infra\1-deploy.ps1
```

---

### 2. Configure GitHub for CI/CD

Run `2-service-principal.ps1` to:

- Confirm you're authenticated with GitHub CLI (`gh`)
- Create an Azure Service Principal with Contributor rights scoped to the resource group
- Upload the credentials as the `AZURE_CREDENTIALS` GitHub secret

```powershell
.\infra\2-service-principal.ps1
```

> ⚠️ Note: You must have [GitHub CLI](https://cli.github.com/) installed and authenticated with `gh auth login` before running this script.

---

### 3. Deploy via GitHub Actions

Once GitHub is configured with `AZURE_CREDENTIALS`, any push to the `main` branch or a manual trigger will:

- Authenticate to Azure
- Build and tag a Docker image
- Push the image to ACR
- Update the Azure Container App with the latest image

CI/CD is handled via the `build-and-deploy.yml` GitHub Actions workflow in `.github/workflows/`.

---

## ✅ Result

After setup, infrastructure management and app deployment are fully automated. You can iterate quickly by committing to `master` or by triggering the workflow manually.

For architecture details and query examples, see [README.md](../README.md).
