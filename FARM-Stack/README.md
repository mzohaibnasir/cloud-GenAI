# F-A-R-M STACK

# NoSQL

stands for "Not Only SQL". It's a type of database that allows for flexible schema design and doesn't require the rigid table-based structure of traditional relational databases. NoSQL databases are designed to handle large amounts of unstructured or semi-structured data and are often used in big data and real-time web applications.

# MongoDB is a NoSQL database

It is based on document model i.e. collection of docs. It uses a document-oriented data model, where data is stored in JSON-like documents called BSON (Binary Serialized Object Notation). This allows for flexible and dynamic schema design, and makes it well-suited for handling large amounts of semi-structured or unstructured data.
In MongoDB, data is organized into collections, which are similar to tables in relational databases. Each collection contains a set of documents, which are similar to rows in a relational database. However, unlike relational databases, MongoDB documents can have different fields and structures, and can be modified dynamically without requiring a fixed schema.
Some key features of MongoDB's document model include:

1. Flexible schema: MongoDB's schema is dynamic and can be modified at runtime, allowing for easy adaptation to changing data structures and requirements.
2. Hierarchical data: MongoDB's document model allows for hierarchical data structures, where documents can contain embedded documents and arrays.
3. Scalability: MongoDB is designed for horizontal scaling, making it suitable for large and distributed datasets.
4. High performance: MongoDB's document model and indexing capabilities allow for fast query performance and data retrieval.
   Overall, MongoDB's document model and NoSQL design make it a popular choice for modern web and mobile applications, big data analytics, and real-time data processing.

# Installtion

1. Install compass
2. Install community edition

3. `mongosh ` to access mongo shell
   1. show dbs

##########################################################################333

# `fastapi.middleware.cors import CORSMiddleware`

## What is CORS?

CORS is a security mechanism implemented by web browsers that restricts web pages from making requests to a different domain than the one that served the web page. This prevents malicious scripts from stealing data from other websites.
CORS (Cross-Origin Resource Sharing) is a security feature implemented in web browsers to prevent web pages from making requests to a different origin (domain, protocol, or port) than the one the web page was loaded from. This is a security feature to prevent malicious scripts from making unauthorized requests on behalf of the user.
FastAPI's CORSMiddleware class is used to enable CORS support in FastAPI applications. By using this middleware, you can specify which origins are allowed to make requests to your API, and which methods (GET, POST, etc.) are allowed.

This code enables CORS support for the FastAPI application, allowing requests from any origin, with any method, and with any headers. The max_age parameter specifies the maximum age of the CORS configuration (in seconds).

Why use CORSMiddleware?

If your FastAPI application is intended to be accessed from a different domain (frontend website) than the one it's hosted on, you need to configure CORS to allow those cross-origin requests. Without proper CORS configuration, the browser will block requests from the frontend to your FastAPI backend, preventing your application from functioning as intended.

`app = FastAPI()`
`origins = ["https://your-frontend-domain.com"]`
`app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])`

# ORIGIN is just a combination of `protocol` + `domain` + `port`

protocol:(http,https)
domain:(app.com)
port:(800)

React might have port:3000 and our FastAPI might have port:5000, we need backend permission to interact with different port

###########################################################################33

The difference between the two is the way the response model is specified.

# `@app.get("/api/todo{title}", response_model=baseTodoClass)`

In this syntax, the response_model parameter is explicitly specified as part of the @app.get decorator. This tells FastAPI to use the baseTodoClass class as the response model for this endpoint.

# `@app.get("/api/todo{title}") -> baseTodoClass`

In this syntax, the response model is specified using the `->` syntax, which is a shorthand way to specify the response model. This is equivalent to the first syntax, but is a more concise way to specify the response model.
Both syntaxes achieve the same result, which is to specify the response model for the endpoint. However, the first syntax is more explicit and clear, while the second syntax is more concise and shorthand.
