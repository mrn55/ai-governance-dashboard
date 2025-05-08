param location string = resourceGroup().location
param appName string
param sku string = 'B2'

resource servicePlan 'Microsoft.Web/serverfarms@2022-03-01' = {
    name: '${appName}-plan'
    location: location
    sku: {
        name: sku
        tier: 'Basic'
    }
    kind: 'linux'
    properties: {
        reserved: true
    }
}

resource webApp 'Microsoft.Web/sites@2022-03-01' = {
    name: appName
    location: location
    kind: 'app,linux'
    properties: {
        serverFarmId: servicePlan.id
        siteConfig: {
        linuxFxVersion: 'PYTHON|3.10'
        appCommandLine: 'gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.api.main:app'
        }
        httpsOnly: true
    }
}