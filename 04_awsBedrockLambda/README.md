# AWS ecosystem: end-to-end project

## Project scope and steps

1. we are doing blog generation

2. we will be creating an API endpoint using API Gateway
3. hitting API will trigger lambda function
4. lambda will be interacting with AWS bedrock API
   1. our all Foundation Models are available in bedrock
5. we'll bw saving response in s3 text as .txt file

##### AWS bedrock: provides lots of foundation models. it directly gives an API

##### AWS sagemaker: It gives enviroment to deploy FM

##### Cloudwatch to monitor logs
