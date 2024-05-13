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
