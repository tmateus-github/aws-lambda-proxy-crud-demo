# AWS lambda CRUD proxy
Fully functional Serverless CRUD API with the following operations (as example):

* POST /movies
* GET /movies?movie_uuid={uuid}
* PUT /movies
* DELETE /movies?movie_uuid={uuid}


![flow chart](./apigw-lambda.png)

## Tecnologies used
* **AWS Lambda** for running code without provisioning servers.
* **AWS API Gateway** for serverless API creation and management.
* **AWS IAM** for creating roles for the lambdas functions.
* **AWS DynamoDB** for a managed NoSQL database.

## Deploying
In order to deploy, we will need to run the following commands:
* This command is going to prepare the package and upload into S3 bucket.
```bash
aws cloudformation package --template-file template.yaml --s3-bucket <BUCKET_NAME> --output-template-file packaged-template.yaml
```
* This command will deploy all the stack.
```bash
aws --region eu-west-1 cloudformation deploy --template-file packaged-template.yaml --stack-name <STACK_NAME> --capabilities CAPABILITY_IAM
```
