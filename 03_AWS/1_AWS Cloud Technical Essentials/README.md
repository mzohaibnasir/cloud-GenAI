## Amazon API Gateway

is a service offered by Amazon Web Services (AWS) that simplifies the process of creating, publishing, maintaining, monitoring, and securing APIs at any scale [1]. An API, or Application Programming Interface, acts as a middleman between applications and backend services. It essentially provides a way for applications to access data, functionality, or business logic from backend resources.

### Here are some of the key features of API Gateway:

1. Supports multiple API types: Create `RESTful APIs`, which are a popular architectural style for APIs, or `WebSocket APIs`, which enable real-time two-way communication between applications.
2. Acts as a front door: API Gateway centralizes access to your backend services, such as those running on EC2 instances, Lambda functions, or web applications.
3. Manages API traffic: API Gateway handles many of the heavy lifting tasks associated with APIs, including traffic management, security features like authorization and access control, throttling to prevent overload, monitoring, and API version management.
4. Cost-effective: There are no minimum fees or startup costs to use API Gateway. You are only charged for the API calls you receive and the data transferred.

If you're looking to build APIs for your own applications or open them up to third-party developers, AWS API Gateway is a powerful tool that can streamline the process.

# An Avaibility Zone

is a geographically separate location within an AWS Region. These zones are isolated from each other to ensure an outage in one zone doesn't disrupt others. Each AZ consists of one or more data centers with redundant power, networking, and physical separation. Imagine them as mini-regions within a larger AWS Region.

## Benefits:

1. Enhanced Fault Tolerance: If an AZ experiences a power outage or hardware failure, your application can seamlessly continue functioning in another zone.
2. Reduced Latency: Since AZs are geographically close within a region, resources in different zones enjoy low-latency network connections. This is crucial for real-time applications.
3. Scalability Made Easy: Scaling your applications up or down becomes effortless by provisioning resources across multiple AZs. Need more compute power? Add resources in another zone!

   In essence, AZs are the foundation for building robust and fault-tolerant applications on AWS.

# REGiON

IF AZ goes down, using redundancy like data centeres, AWS also clusters AZs together. and also connects them with redundant
high speed and low latency links. A cluster of AZs is called Region.

# Latency refers to the time delay it takes for data to travel from one point to another across a network.

###################################################################################

# WAYS TO INTERACT WITH AWS"

1. AWS Management console
2. AWS CLI
3. SDK

###################################################################################

# AWS IDENTITY & ACCESS Control and Credential management

# IAM

All API calls in AWS must be signed and authenticated in order to be allowed; no matter if the resources live in the same account or not. Application code running on the EC2 instance nneds access to credentials to make this signed call to S3.IAM does that.

# Aplication lvl Managment(authenticating users into the application itself) is not managed by IAM

# IAM handles access to AWS account and READ/WRITE between different AWS services.

## Authentication:You are who you say you are

IAM users take care of authentication

## Authorization: Are you autherized to launch this task.

you can take care of authorization by attatching IAM policies to users in order to grant or deny permissions to take actions. IAM policies are json based docs

# ROLE BASED IAM USERS: to handle signed API calls between resouces.

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

# IAM users have associated credentials like an access key ID and secret access key that re used to sign requests.

# ROLE BASED ACCESS IN AWS:

Policies can be assigned to users and group to assign permissions.
An IAM role is an identity that can be assumed by someone/something who needs temp access to AWS credentials.

## so how does the process of signing API calls work

# IAM roles handle this signing process. IAM roles are identities in AWS that like an IAM user also have asssociated AWS credentials used to sign requests.

# IAM users have usernames & password as well as static credentials.IAM ROLES don't have static one. Credentials are programmmatic, temporary and automatically rotated. EC2 instance will be assigned an IAM role which will help app runnning on it get access to S3.

# External Identity providers can also assume IAM role

###########WEEK2

# CPV: Virtual Private Cloud

Imagine you have your own little apartment in a giant apartment building, that's kind of like a VPC in AWS. VPC stands for Virtual Private Cloud. It's a private network you create within the AWS cloud, separate from the public internet.

Here's why VPCs are useful:

##### Security: They keep your resources, like virtual machines, isolated from others in the cloud. Think of your apartment building having its own security system, keeping things safe and sound.

##### Control: You have control over who can access your resources. It's like having your own keys to your apartment, deciding who can visit.

##### Flexibility: You can customize your network within the VPC, like adding different rooms (subnets) for different purposes in your apartment.

So, VPCs provide a secure and customizable space for your AWS resources, just like your own little apartment in the cloud!

# VPC (Virtual Private Cloud) in AWS is a virtual network dedicated to your AWS account. It allows you to define a virtual network topology, including subnets, route tables, and gateways, that is logically isolated from other virtual networks in the AWS Cloud.

# In container everything is just packaged up in a single executable, container itself.

container orchestration: Managing multiple containers.
Amazon container orchestration tools:

1. Amazon Rlastic container service
2. Amazon Kubernetes service
3. AWS Fargate

# AWS Fargate: sreverless compute platform for ECS or EKS

is a technology that allows you to run containers without managing servers or clusters of Amazon EC2 instances ¹. It provides on-demand, right-sized compute capacity for containers, and you don't have to provision, configure, or scale groups of virtual machines on your own to run containers ². Here are some key points about AWS Fargate ³:
#############################

# ORCHESTRATE CONTAINERS

In AWS, containers run on EC2 instances. For example, you may have a large instance and run a few containers on that instance.While running one instance is easy to manage, it lacks high availability and scalability. Most companies and organizations run many containers on many EC2 instances across several Availability Zones.If you’re trying to manage your compute at a large scale, you need to know:

How to place your containers on your instances.

What happens if your container fails.

What happens if your instance fails.

How to monitor deployments of your containers.

This coordination is handled by a container orchestration service. AWS offers two container orchestration services: Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS).

MANAGE CONTAINERS WITH AMAZON ELASTIC CONTAINER SERVICE (AMAZON ECS)
Amazon ECS is an end-to-end container orchestration service that allows you to quickly spin up new containers and manage them across a cluster of EC2 instances.

To run and manage your containers, you need to install the Amazon ECS Container Agent on your EC2 instances. This agent is open source and responsible for communicating back to the Amazon ECS service about cluster management details. You can run this agent on both Linux and Windows AMIs. An instance with the container agent installed is often called a container instance.

Once the Amazon ECS container instances are up and running, you can perform actions that include, but are not limited to, launching and stopping containers, getting cluster state, scaling in and out, scheduling the placement of containers across your cluster, assigning permissions, and meeting availability requirements.

To prepare your application to run on Amazon ECS, you create a task definition. The task definition is a text file, in JSON format, that describes one or more containers. A task definition is similar to a blueprint that describes the resources you need to run that container, such as CPU, memory, ports, images, storage, and networking information.

# AWS serverless

Serverless Computing on AWS: Unleash Your Code, Ditch the Servers
Serverless computing on AWS is a development approach where you focus on writing and deploying code, and AWS takes care of the servers behind the scenes. Here's the gist:

1. You write the code: Think of it as the delicious recipe for your application.
2. AWS provides the kitchen: They handle the servers, scaling, and management – all the infrastructure needed to cook your application.
   3.You only pay for what you use: Just like at a restaurant, you're charged based on the resources your code consumes while it executes (cooking time).

Benefits of Serverless on AWS:

1. Simplified Management: No more server headaches! Focus on your code and application logic.
2. Increased Agility: Faster development and deployment cycles. Get your app out there quicker!
3. Cost-Effectiveness: Pay-per-use model saves you money on idle servers. Only pay for the "cooking time" of your code.
4. Automatic Scaling: AWS scales your application up or down based on demand. No need to worry about server capacity.

#########################

# ECS or EKS is the container orchestrator. It manges container;s lifecycle. Then you need computer platform, this is where containers run.

# ECS or EKS run containers on EC2 clusters but EC2 is not serverless

# AWS fargate is SERVERLESS: it is a serverless compute platform for containers that you can use with either ECS or EKS. With AWS fargate you run containers on managed serverlesss compute platform. Scaling and fault tolerance is built in and no need to worry about underlying OS.

# Amazon ECR: Elastic container Registry: a repository to store container images to be pulled and deployed from.

then , in fargate to run these conatiners, you define memory and compute resources for your task if you are using ECS or your pod if you are using EKS. Then you run your containers,
