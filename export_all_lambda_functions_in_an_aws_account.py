
#This version downloads oonly the functions from a single region as per your `aws configure` settings

import boto3
import requests

client = boto3.client('lambda')

list_of_functions = client.list_functions(
    FunctionVersion='ALL',
    MaxItems=123
)

function_names = []

for function_ in list_of_functions['Functions']:
    function_names.append(function_['FunctionName'])

print(function_names)

for function_name in function_names:
    lambda_func = client.get_function(FunctionName=function_name)
    my_func_code = requests.get(lambda_func['Code']['Location'])
    open('/some/directory/' + function_name + '.zip', 'wb').write(my_func_code.content)



