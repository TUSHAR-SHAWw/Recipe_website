pip install -r requirements.txt
python3.9 manage.py collectstatic
pip install --upgrade awscli
npm install -g aws-cli
export PATH=$PATH:$(npm prefix -g)/bin
aws lambda update-function-configuration --function-name YourFunctionName --timeout NewTimeoutInSecond
