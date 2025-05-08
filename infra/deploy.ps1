$ResourceGroup = "ai-governance-demo"
$Location = "centralus"
$AppName = "neal-fastapi-demo"

# Create resource group
az group create --name $ResourceGroup --location $Location

# Deploy infrastructure using Bicep
az deployment group create `
  --resource-group $ResourceGroup `
  --template-file ./main.bicep `
  --parameters appName=$AppName