# How to setup?
## Initialize terraform
```sh
terraform init

```

## Generate a SSH key
My suggestion is to save locally, you will need to ssh into your server
```sh
ssh-keygen -t rsa -b 2048

```

## Authorize AWS
```sh
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
```

## Plan/Apply changes
```sh
terraform apply
```

## Connect to you server
Retrieve server IP
```sh
terraform output
```

SSH into
```sh
ssh -i your-private-key.pem ec2-user@35.156.53.127
```