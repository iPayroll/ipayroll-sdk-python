# Introduction

The iPayroll Restful Api allows you manipulate some of your iPayroll data through
third party application. In order to start a quick Java project with iPayroll
Restful api, we created the iPayroll java sdk project to help you quickly start
a project to interact with iPayroll Restful API by Python.

## Documentations

All of iPayroll Restful Api documentation can be found at [here](http://dev.ipayroll.co.nz).


## Usage

### Configuration

```python
from ipayroll_sdk.client import Client
client = Client('d908376c-3d1b-41a9-8358-1fad946e0c57', 'GwUmPqD8s7mGj4d', 'http://localhost:3000')
```

### Authentication

```python
def connect(self):
  auth_url = client.oauth2().get_authorization_url()
  return redirect(auth_url)
end
```
When the redirect_uri is called with the code parameter
```python
client.oauth2().exchange_authorization_code_for_access_token(request.GET.get('code'))
```

refresh the access token

```python
client.oauth2().refresh_access_token()
```

To get access_token you can:
```python
def token_saver(self, token):
    ...

client = Client('d908376c-3d1b-41a9-8358-1fad946e0c57', 'GwUmPqD8s7mGj4d',
    'http://localhost:3000', token_updater=token_saver )
```

### Request a list of resource
Get the first page of 20 elements
```python
client.employees().list()
```
Get a specific page
```python
client.employees().list(page=2, size=10)
```
### Request a resource
```python
cost_center_id = '7242'
client.cost_centres.get(cost_center_id)
```

### Create resources
```python
from ipayroll_sdk.models import CostCentre
cc = CostCentre()
cc.code='code1'
cc.description='desc1'
cc.displayValue='dispVal1'

created_cost_center = client.costcentres().create(cc)

cc2 = CostCentre()
cc2.code='code2'
cc2.description='desc2'
cc2.displayValue='dispVal2'

cc3 = CostCentre()
cc3.code='code3'
cc3.description='desc3'
cc3.displayValue='dispVal3'

created_cost_centers = client.costcentres().create([cc1, cc2])
```

## Development
wheel package need to be installed
```bash
$ pip install wheel
```

make can be used to build:
```bash
$ make build
```