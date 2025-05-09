$resourceGroup = "ai-governance-demo"
$acrName = "nealregistry"
$containerAppName = "neal-api"
$envName = "default-env"

# Deploy Container App
az containerapp update `
  --name $containerAppName `
  --resource-group $resourceGroup `
  --image "$acrName.azurecr.io/sample/fastapi-azure:latest" `
  --registry-server "$acrName.azurecr.io" `
  --registry-username (az acr credential show --name $acrName --query "username" -o tsv) `
  --registry-password (az acr credential show --name $acrName --query "passwords[0].value" -o tsv)