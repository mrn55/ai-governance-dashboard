# Check GitHub CLI auth
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

$resourceGroup = "ai-governance-demo"
$subscriptionId = (az account show --query id -o tsv)

$spJson = az ad sp create-for-rbac `
  --name "github-deployer" `
  --role contributor `
  --scopes "/subscriptions/$subscriptionId/resourceGroups/$resourceGroup" `
  --sdk-auth
$spJsonSingleLine = ($spJson | ConvertFrom-Json | ConvertTo-Json -Compress)

$repo = "mrn55/ai-governance-dashboard"

gh secret set AZURE_CREDENTIALS -b $spJsonSingleLine --repo $repo