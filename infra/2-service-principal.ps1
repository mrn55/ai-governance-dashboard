# Ensure GitHub CLI is authenticated
try {
    gh auth status --hostname github.com > $null 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "GitHub CLI is not authenticated. Run 'gh auth login' and try again." -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "GitHub CLI not installed or failed to run." -ForegroundColor Red
    exit 1
}

# Define variables
$resourceGroup = "ai-governance-demo"
$subscriptionId = (az account show --query id -o tsv)
$repo = "mrn55/ai-governance-dashboard"

# Create Azure service principal and capture output
$spJson = az ad sp create-for-rbac `
  --name "github-deployer" `
  --role contributor `
  --scopes "/subscriptions/$subscriptionId/resourceGroups/$resourceGroup" `
  --sdk-auth

# Encode the JSON as base64
$jsonBytes = [System.Text.Encoding]::UTF8.GetBytes($spJson)
$base64Json = [Convert]::ToBase64String($jsonBytes)

# Set the secret as base64-encoded value
gh secret set AZURE_CREDENTIALS_BASE64 --repo $repo --body $base64Json