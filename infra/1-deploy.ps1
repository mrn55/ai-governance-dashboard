$resourceGroup = "ai-governance-demo"
$location = "centralus"
$acrName = "nealregistry"
$envName = "default-env"
$containerAppName = "neal-api"

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
