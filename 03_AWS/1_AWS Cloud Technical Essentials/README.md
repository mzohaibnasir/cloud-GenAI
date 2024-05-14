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

# IAM users have usernames & password as well as static credentials.IAM ROLES don't have static one.Credentials are temporary and automatically rotated.
