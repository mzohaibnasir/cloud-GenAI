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
`192.168.1.0/24` here `192.168.1` are fixed bits while `0` is flexible

It begins with a starting IP address and is separated by a forward slash (the “/” character) followed by a number. The number at the end specifies how many of the bits of the IP address are fixed. In this example, the first 24 bits of the IP address are fixed. The rest are flexible.

32 total bits subtracted by 24 fixed bits leaves 8 flexible bits. Each of these flexible bits can be either 0 or 1, because they are binary. That means you have two choices for each of the 8 bits, providing 256 IP addresses in that IP range.

The higher the number after the /, the smaller the number of IP addresses in your network. For example, a range of 192.168.1.0/24 is smaller than 192.168.1.0/16.

When working with networks in the AWS Cloud, you choose your network size by using CIDR notation. In AWS, the smallest IP range you can have is /28, which provides you 16 IP addresses. The largest IP range you can have is a /16, which provides you with 65,536 IP addresses.

## Virtual Private Cloud(VPC)

#### VPC is the network that enables internet traffic to float into your application.

VPC is like walls around data center. In data centers, walls act as a boundary between outside world and all of your infrastructure. A VPC acts as a boundary where your applications and resources are isolated from any outside movement. Nothinng comes into the VPC and nothing goes out without your explicit permission.

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

#### To create a VPC:

1. first, you have to declare two specific settings.

   1. Region
   2. IP range for VPC in form of CIDR notation.

Then divide your space inside VPC into smaller segments called subnets.You put your resources inside of these subnets. The goal of these subnets is to provide more granular control over access to your resources. So, if we have public resources that require internet connectivity like our employee directory app that we want to be accessed over public internet, we can put them in a subnet with internet connectivity. For our more private resources, I can create another subnet and have different controls to keep those resources private.

Subnets are a fundamental building block within a VPC (Virtual Private Cloud) on cloud platforms. They act like logical partitions within your VPC, allowing you to further segment your network resources.Imagine carving your VPC network into smaller, more manageable sections. Each subnet represents one such section with a designated pool of IP addresses. You can launch resources like EC2 instances (AWS) or virtual machines (other providers) within these subnets.

2. Subnet:
   After you create your VPC, you need to create subnets inside of this network. Think of subnets as smaller networks inside your base network—or virtual area networks (VLANs) in a traditional, on-premises network. In an on-premises network, the typical use case for subnets is to isolate or optimize network traffic. In AWS, subnets are used for high availability and providing different connectivity options for your resources. When you create a subnet, you need to choose three settings.

   1. The VPC you want your subnet to live in, in this case VPC (10.0.0.0/16).

   2. The Availability Zone you want your subnet to live in, in this case AZ1.

   3. A CIDR block for your subnet, which must be a subset of the VPC CIDR block, in this case 10.0.0.0/24.

When you launch an EC2 instance, you launch it inside a subnet, which will be located inside the Availability Zone you choose.  
 To create a subnet: you need three main things:

1.  VPC you want your subnet to live in
2.  AZ you want yout subnet to live in.
3.  CIDR range for your subnet which would be subnet of the VPC CIDR range.
    public subnet: `10.1.1.0/24`
    private subnet: `10.1.3.0/24`

#### Right now, only resources inside VC have acces to our WebAPP. To enable outside access, we need a component called internet gateway. Ypu need to attatch your gateway to VPC.

### Internet Gateway connects you VPC to internet.

An internet gateway in a VPC (Virtual Private Cloud) acts as the entry and exit point for internet traffic. It's a crucial component if you need resources within your VPC to communicate with the wider internet. Here's a closer look at internet gateways:

#### Purpose:

1. Enables resources in your VPC, like EC2 instances, to initiate outbound connections to the internet (e.g., downloading updates, accessing web services).
2. Allows inbound connections to your VPC resources from the internet (if configured with security groups and route tables to permit it).

#### What if we want to only allow traffic between data center and VPC, we'll use virtual Private gateway(VGW):

VGW allows you to create VPN connection between private network(like data center) and VPC. With help of VGW, you can establish encrypted VPN connection to your private internal AWS resources.

## So we have VPC, 2 subnets and an internet gateway. We'll do all this in another AZ

---

# Reserved IPs

For AWS to configure your VPC appropriately, AWS reserves five IP addresses in each subnet. These IP addresses are used for routing, Domain Name System (DNS), and network management.

For example, consider a VPC with the IP range 10.0.0.0/22. The VPC includes 1,024 total IP addresses. This is divided into four equal-sized subnets, each with a /24 IP range with 256 IP addresses. Out of each of those IP ranges, there are only 251 IP addresses that can be used because AWS reserves five.
![alt text](fC4DaI4uRuCRtkolNtRUSA_2ceb6c8eeddf4ffba7175739502a34f1_image.png)

Since AWS reserves these five IP addresses, it can impact how you design your network. A common starting place for those who are new to the cloud is to create a VPC with a IP range of /16 and create subnets with a IP range of /24. This provides a large amount of IP addresses to work with at both the VPC and subnet level.

### Gateways

1. Internet Gateway

   To enable internet connectivity for your VPC, you need to create an internet gateway. Think of this gateway as similar to a modem. Just as a modem connects your computer to the internet, the internet gateway connects your VPC to the internet. Unlike your modem at home, which sometimes goes down or offline, an internet gateway is highly available and scalable. After you create an internet gateway, you then need to attach it to your VPC.

2. Virtual Private Gateway

   A virtual private gateway allows you to connect your AWS VPC to another private network. Once you create and attach a VGW to a VPC, the gateway acts as anchor on the AWS side of the connection. On the other side of the connection, you’ll need to connect a customer gateway to the other private network. A customer gateway device is a physical device or software application on your side of the connection. Once you have both gateways, you can then establish an encrypted VPN connection between the two sides.

## Amazon VPC routing:

Traffic has entered into VPC through Internet gateway but that does not mean it entered the right room. We need to provide a path for the internet traffic.It makes sure that traffic enter the internet gateway and reach the right subnet. We do that using route tables

### Route tables

A route table contains a set of rules called routes that are used to determine where the network traffic is directed. These route tables can be applied at subnet levels or VPC level.

When you create a brand new VPC, AWS creates a route table called the main route table.

Route tables are a fundamental part of managing traffic flow within a VPC (Virtual Private Cloud) in AWS. They act like a set of instructions that direct network traffic to its destination. Here's a breakdown of route tables in AWS:

#### Concept:

Imagine a table with entries specifying where to send different types of traffic. Each entry (route) has a destination (CIDR block) and a target (gateway or another subnet) that determines the path for traffic.

#### Key Components:

1. Destination (CIDR block): This specifies the IP address range for which the route applies. For example, "0.0.0.0/0" represents all traffic on the internet.

2. Target: This defines where to send traffic for the specified destination. It can be:
   1. Internet Gateway (IGW): Directs traffic to the internet.
   2. NAT Gateway: Enables outbound traffic from a private subnet to the internet.
   3. Virtual Private Gateway (VGW): Routes traffic to a VPN connection for on-premises network access.
   4. Another Subnet: Routes traffic to a different subnet within the VPC.

#### How Route Tables Work:

1. When a network packet originates from an instance in a subnet, its destination IP address is examined.
2. The subnet's route table is consulted to find a matching route (based on the destination CIDR block).
3. If a match is found, the packet is forwarded to the specified target (gateway or another subnet).
4. The target then handles further routing or transmission of the packet.

#### Main vs. Custom Route Tables:

##### Main Route Table (default):

Every VPC comes with a main route table automatically. It applies to all subnets that are not explicitly associated with a custom route table. The main route table typically doesn't have a route for internet access, so you'll need to create a custom route if you need internet connectivity in your VPC.

##### Custom Route Tables:

You can create custom route tables to have more granular control over traffic flow for specific subnets within your VPC. You can associate one or more subnets with a custom route table.

#### Benefits of Route Tables:

1. Control Traffic Flow: You can define how traffic is routed within your VPC and to the internet.
2. Security: By controlling which subnets have internet access and how traffic flows, you can enhance the security of your VPC resources.
3. Scalability: You can easily add new routes or modify existing ones to adapt to changes in your network configuration.

**Overall, route tables are essential for managing network traffic flow within your VPC in AWS. They provide a mechanism to control where your resources communicate and ensure proper connectivity within your cloud environment.**
