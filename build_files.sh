pip install -r requirements.txt
python3.9 manage.py collectstatic
aws lambda update-function-configuration --function-name YourFunctionName --timeout NewTimeoutInSeconds --memory-size NewMemorySizeInMB
