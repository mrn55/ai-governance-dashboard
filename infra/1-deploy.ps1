$resourceGroup = "ai-governance-demo"
$location = "centralus"
$acrName = "nealregistry"
$envName = "default-env"
$containerAppName = "neal-api"
$uiAppName = "neal-ui"

az group create --name $resourceGroup --location $location

az acr create `
  --resource-group $resourceGroup `
  --name $acrName `
  --sku Basic `
  --admin-enabled true

az provider register -n Microsoft.OperationalInsights --wait

# Create Container App environment
az containerapp env create `
  --name $envName `
  --resource-group $resourceGroup `
  --location $location

# create placeholder container app for api
az containerapp create `
  --name $containerAppName `
  --resource-group $resourceGroup `
  --environment $envName `
  --image "mcr.microsoft.com/hello-world" `
  --target-port 8000 `
  --ingress external `
  --cpu 1.0 `
  --memory 2.0Gi `
  --min-replicas 1

# create placeholder container app for ui
az containerapp create `
  --name $uiAppName `
  --resource-group $resourceGroup `
  --environment $envName `
  --image "mcr.microsoft.com/hello-world" `
  --target-port 8501 `
  --ingress external `
  --cpu 1.0 `
  --memory 2.0Gi `
  --min-replicas 1 `
  --env-vars API_URL="https://$containerAppName.$location.azurecontainerapps.io"
