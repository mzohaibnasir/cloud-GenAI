# AWS

#### Latency refers to the time delay it takes for data to travel from one point to another across a network.

## 1. Amazon API Gateway

is a service offered by Amazon Web Services (AWS) that simplifies the process of creating, publishing, maintaining, monitoring, and securing APIs at any scale [1]. An API, or Application Programming Interface, acts as a middleman between applications and backend services. It essentially provides a way for applications to access data, functionality, or business logic from backend resources.

### Here are some of the key features of API Gateway:

1. Supports multiple API types: Create `RESTful APIs`, which are a popular architectural style for APIs, or `WebSocket APIs`, which enable real-time two-way communication between applications.
2. Acts as a front door: API Gateway centralizes access to your backend services, such as those running on EC2 instances, Lambda functions, or web applications.
3. Manages API traffic: API Gateway handles many of the heavy lifting tasks associated with APIs, including traffic management, security features like authorization and access control, throttling to prevent overload, monitoring, and API version management.
4. Cost-effective: There are no minimum fees or startup costs to use API Gateway. You are only charged for the API calls you receive and the data transferred.

If you're looking to build APIs for your own applications or open them up to third-party developers, AWS API Gateway is a powerful tool that can streamline the process.

## 2. An Avaibility Zone

is a geographically separate location within an AWS Region. These zones are isolated from each other to ensure an outage in one zone doesn't disrupt others. Each AZ consists of one or more data centers with redundant power, networking, and physical separation. Imagine them as mini-regions within a larger AWS Region.

### Benefits:

1. Enhanced Fault Tolerance: If an AZ experiences a power outage or hardware failure, your application can seamlessly continue functioning in another zone.
2. Reduced Latency: Since AZs are geographically close within a region, resources in different zones enjoy low-latency network connections. This is crucial for real-time applications.
3. Scalability Made Easy: Scaling your applications up or down becomes effortless by provisioning resources across multiple AZs. Need more compute power? Add resources in another zone!

   In essence, AZs are the foundation for building robust and fault-tolerant applications on AWS.

## 3. REGION

IF AZ goes down, using redundancy like data centeres, AWS also clusters AZs together. and also connects them with redundant
high speed and low latency links. A cluster of AZs is called Region.

#####################################################################################

## WAYS TO INTERACT WITH AWS

1. AWS Management console
2. AWS CLI
3. SDK

###################################################################################

# AWS IDENTITY & ACCESS Control and Credential management

## IAM

All API calls in AWS must be signed and authenticated in order to be allowed; no matter if the resources live in the same account or not. Application code running on the EC2 instance nneds access to credentials to make this signed call to S3.IAM does that.

### Aplication lvl Managment(authenticating users into the application itself) is not managed by IAM

### IAM handles access to AWS account and READ/WRITE between different AWS services.

### Authentication:You are who you say you are

IAM users take care of authentication

### Authorization: Are you autherized to launch this task.

you can take care of authorization by attatching IAM policies to users in order to grant or deny permissions to take actions. IAM policies are json based docs

## ROLE BASED IAM USERS: to handle signed API calls between resouces.

# IAM policy

{

"Version": "2012-10-17",

     "Statement": [{
          "Effect": "Allow",

          "Action": "*",

          "Resource": "*"

     }]

}

In this policy, there are four major JSON elements: Version, Effect, Action, and Resource.

The Version element defines the version of the policy language. It specifies the language syntax rules that are needed by AWS to process a policy. To use all the available policy features, include "Version": "2012-10-17" before the "Statement" element in all your policies.

The Effect element specifies whether the statement will allow or deny access. In this policy, the Effect is "Allow", which means you’re providing access to a particular resource.

The Action element describes the type of action that should be allowed or denied. In the above policy, the action is "\*". This is called a wildcard, and it is used to symbolize every action inside your AWS account.

The Resource element specifies the object or objects that the policy statement covers. In the policy example above, the resource is also the wildcard "\*". This represents all resources inside your AWS console.

### IAM users have associated credentials like an access key ID and secret access key that re used to sign requests.

## ROLE BASED ACCESS IN AWS:

Policies can be assigned to users and group to assign permissions.
An IAM role is an identity that can be assumed by someone/something who needs temp access to AWS credentials.

### so how does the process of signing API calls work

### IAM roles handle this signing process. IAM roles are identities in AWS that like an IAM user also have asssociated AWS credentials used to sign requests.

### IAM users have usernames & password as well as static credentials.IAM ROLES don't have static one. Credentials are programmmatic, temporary and automatically rotated. EC2 instance will be assigned an IAM role which will help app runnning on it get access to S3.

### External Identity providers can also assume IAM role

# W-EE-K 2

## VPC: Virtual Private Cloud

Imagine you have your own little apartment in a giant apartment building, that's kind of like a VPC in AWS. VPC stands for Virtual Private Cloud. It's a private network you create within the AWS cloud, separate from the public internet.

Here's why VPCs are useful:

1. Security: They keep your resources, like virtual machines, isolated from others in the cloud. Think of your apartment building having its own security system, keeping things safe and sound.

2. Control: You have control over who can access your resources. It's like having your own keys to your apartment, deciding who can visit.

3. Flexibility: You can customize your network within the VPC, like adding different rooms (subnets) for different purposes in your apartment.

So, VPCs provide a secure and customizable space for your AWS resources, just like your own little apartment in the cloud!

### VPC (Virtual Private Cloud) in AWS is a virtual network dedicated to your AWS account. It allows you to define a virtual network topology, including subnets, route tables, and gateways, that is logically isolated from other virtual networks in the AWS Cloud.

## Containers.

### In container everything is just packaged up in a single executable, container itself.

### container orchestration: Managing multiple containers.

Amazon container orchestration tools:

1. Amazon Elastic container service
2. Amazon Kubernetes service
3. AWS Fargate

### AWS Fargate: sreverless compute platform for ECS or EKS

is a technology that allows you to run containers without managing servers or clusters of Amazon EC2 instances ¹. It provides on-demand, right-sized compute capacity for containers, and you don't have to provision, configure, or scale groups of virtual machines on your own to run containers ². Here are some key points about AWS Fargate ³:

## ORCHESTRATE CONTAINERS

In AWS, containers run on EC2 instances. For example, you may have a large instance and run a few containers on that instance.While running one instance is easy to manage, it lacks high availability and scalability. Most companies and organizations run many containers on many EC2 instances across several Availability Zones.If you’re trying to manage your compute at a large scale, you need to know:

1. How to place your containers on your instances.

2. What happens if your container fails.

3. What happens if your instance fails.

4. How to monitor deployments of your containers.

This coordination is handled by a container orchestration service. AWS offers two container orchestration services: Amazon `Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS)`.

### MANAGE CONTAINERS WITH AMAZON ELASTIC CONTAINER SERVICE (AMAZON ECS)

Amazon ECS is an end-to-end container orchestration service that allows you to quickly spin up new containers and manage them across a cluster of EC2 instances.

To run and manage your containers, you need to install the Amazon ECS Container Agent on your EC2 instances. This agent is open source and responsible for communicating back to the Amazon ECS service about cluster management details. You can run this agent on both Linux and Windows AMIs. An instance with the container agent installed is often called a container instance.

Once the Amazon ECS container instances are up and running, you can perform actions that include, but are not limited to, launching and stopping containers, getting cluster state, scaling in and out, scheduling the placement of containers across your cluster, assigning permissions, and meeting availability requirements.

To prepare your application to run on Amazon ECS, you create a task definition. The task definition is a text file, in JSON format, that describes one or more containers. A task definition is similar to a blueprint that describes the resources you need to run that container, such as CPU, memory, ports, images, storage, and networking information.

## AWS serverless

Every definition of serverless mentions four aspects.

1. No servers to provision or manage.

2. Scales with usage.

3. You never pay for idle resources.

4. Availability and fault tolerance are built-in.

### Serverless Computing on AWS: Unleash Your Code, Ditch the Servers

### Serverless computing on AWS is a development approach where you focus on writing and deploying code, and AWS takes care of the servers behind the scenes. Here's the gist:

1. You write the code: Think of it as the delicious recipe for your application.
2. AWS provides the kitchen: They handle the servers, scaling, and management – all the infrastructure needed to cook your application.
3. You only pay for what you use: Just like at a restaurant, you're charged based on the resources your code consumes while it executes (cooking time).

### Benefits of Serverless on AWS:

1. Simplified Management: No more server headaches! Focus on your code and application logic.
2. Increased Agility: Faster development and deployment cycles. Get your app out there quicker!
3. Cost-Effectiveness: Pay-per-use model saves you money on idle servers. Only pay for the "cooking time" of your code.
4. Automatic Scaling: AWS scales your application up or down based on demand. No need to worry about server capacity.

### ECS or EKS is the container orchestrator. It manges container;s lifecycle. Then you need computer platform, this is where containers run.

### ECS or EKS run containers on EC2 clusters but EC2 is not serverless

### Amazon ECR: Elastic container Registry: a repository to store container images to be pulled and deployed from.

## AWS fargate is SERVERLESS:

wit is a serverless compute platform for containers that you can use with either ECS or EKS. With AWS fargate you run containers on managed serverlesss compute platform. Scaling and fault tolerance is built in and no need to worry about underlying OS.then , in fargate to run these conatiners, you define memory and compute resources for your task if you are using ECS or your pod if you are using EKS. Then you run your containers,

## EXPLORE SERVERLESS CONTAINERS WITH AWS FARGATE

Amazon ECS and Amazon EKS enable you to run your containers in two modes.

1. Amazon EC2 mode

2. AWS Fargate mode

AWS Fargate is a purpose-built serverless compute engine for containers. Fargate scales and manages the infrastructure, allowing developers to work on what they do best: application development.It achieves this by allocating the right amount of compute, eliminating the need to choose and handle EC2 Instances and cluster capacity and scaling. Fargate supports both Amazon ECS and Amazon EKS architecture and provides workload isolation and improved security by design.

AWS Fargate abstracts the EC2 instance so you’re not required to manage it. However, with AWS Fargate, you can use all the same ECS primitives, APIs, and AWS integrations. It natively integrates with AWS Identity and Access Management (IAM) and Amazon Virtual Private Cloud (VPC). Having native integration with Amazon VPC allows you to launch Fargate containers inside your network and control connectivity to your applications.

## AWS LAMBDA

AWS Lambda is a serverless computing service provided by Amazon Web Services (AWS). It allows users to run code without provisioning or managing servers, and only charges for the compute time consumed by the code.

If you want to deploy your workloads and applications without having to manage any EC2 instances or containers, you can use AWS Lambda.AWS Lambda lets you run code without provisioning or managing servers or containers. You can run code for virtually any type of application or backend service, including data processing, real-time stream processing, machine learning, WebSockets, IoT backends, mobile backends, and web apps, like your corporate directory app!

AWS Lambda requires zero administration from the user. You upload your source code and Lambda takes care of everything required to run and scale your code with high availability. There are no servers to manage, bringing you continuous scaling with subsecond metering and consistent performance

#### Lambda allows you to package and upload your code to the Lambda service, creating what is called lambda function.

#### It is uusede when you dont need code to be running 24/7. It runs whenever event is triggered

i.e. Resize image whenever it is uploaded in s3 bucket. It will resize it and will store it at some other place in s3 bucket

#### A trigger integrates your Lambda function with other AWS services, enabling you to run your Lambda function in response to certain API calls that occur in your AWS account.

#### Here are some key features of AWS Lambda:

1. Serverless: No need to provision or manage servers
2. Event-driven: Code is executed in response to events (e.g. API calls, database updates, file uploads)
3. Scalable: Automatically scales to handle large workloads
4. High availability: Code is executed in multiple availability zones
5. Supports multiple programming languages: Node.js, Python, Java, Go, Ruby, and more
6. Integrated with AWS services: Can be used with other AWS services like API Gateway, S3, DynamoDB, and more

#### AWS Lambda is commonly used for:

1. Real-time data processing: Processing data in real-time, such as image or video processing
2. APIs: Creating RESTful APIs and handling API requests
3. Background tasks: Running tasks in the background, such as sending emails or processing files
4. IoT: Handling IoT device data and processing it in real-time

#### AWS Lambda function handler

The AWS Lambda function handler is the method in your function code that processes events. When your function is invoked, Lambda runs the handler method. When the handler exits or returns a response, it becomes available to handle another event.You can use the following general syntax when creating a function handler in Python:

`def handler_name(event, context): ... return some_value`

---

# NETWORKING ON AWS

#### ipv4:

It’s called 32-bit because you have 32 digits `10101010 10101010 10101010 10101010`
in binary but in decoimal they look something like `192.168.0.1`

#### CIDR(Classless Inter-Domain Routing (CIDR) notation) NOTATION

192.168.1.30 is a single IP address. If you wanted to express IP addresses between the range of 192.168.1.0 and 192.168.1.255, how can you do that?

One way is by using Classless Inter-Domain Routing (CIDR) notation. CIDR notation is a compressed way of specifying a range of IP addresses. Specifying a range determines how many IP addresses are available to you.

CIDR notation looks like this:

## Virtual Private Cloud(VPC)

#### VPC is the bnetwork that enables internet traffic to float into your application.

A Virtual Private Cloud (VPC) is a virtual network dedicated to your AWS account. It allows you to define a virtual network topology, including subnets, route tables, and gateways, which are logically isolated from other virtual networks in the AWS Cloud.

#### lambda does not need network at all

Here are some key features of VPC:

1. Virtual network: A logically isolated section of the AWS Cloud
2. Subnets: Divide your VPC into smaller, isolated networks
3. Route tables: Control how traffic is routed within your VPC
4. Gateways: Connect your VPC to the internet or other networks
5. Security groups: Control inbound and outbound traffic at the instance level
6. Network ACLs: Control inbound and outbound traffic at the subnet level
7. Supports multiple IP addresses: Including IPv4 and IPv6
