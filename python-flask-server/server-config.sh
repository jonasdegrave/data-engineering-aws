# Install PIP
sudo apt install python3-pip -y

# Install AWS CLI
sudo apt install awscli -y

# Perform 'aws configure' automatically setting these fields correctly:
aws configure set region eu-central-1
aws configure set output table

# TODO: Configure this correctly into EC2 ambient variables:
#aws configure set aws_access_key_id     $AWS_ACCESS_KEY_ID
#aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY

# Install AWS SDK for Python (boto3)
pip3 install boto3

# Install the requirements for Flask
pip3 install -r ~/data-engineering-aws/python-flask-server/requirements.txt