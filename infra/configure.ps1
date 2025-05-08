$ResourceGroup = "ai-governance-demo"
$AppName = "neal-fastapi-demo"

# (Optional) Add environment variables
az webapp config appsettings set `
  --name $AppName `
  --resource-group $ResourceGroup `
  --settings ENV=production DEBUG=false

# (Optional) Set startup command in case Bicep didn't apply it
az webapp config set `
  --name $AppName `
  --resource-group $ResourceGroup `
  --startup-file "gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.api.main:app"
