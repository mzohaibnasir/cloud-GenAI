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

######################################################################################################

## Modern versions of Python have support for "asynchronous code" using something called "coroutines", with async and await syntax.

Let's see that phrase by parts in the sections below:

1. Asynchronous Code:
   Asynchronous code is a type of code that allows for concurrent execution of multiple tasks, without blocking the main thread of execution. It's called "asynchronous" because the computer / program doesn't have to be "synchronized" with the slow task, waiting for the exact moment that the task finishes, while doing nothing, to be able to take the task result and continue the work.
2. async and await
3. Coroutines:
   Coroutine is just the very fancy term for the thing returned by an async def function. Python knows that it is something like a function that it can start and that it will end at some point, but that it might be paused ⏸ internally too, whenever there is an await inside of it.

   But all this functionality of using asynchronous code with async and await is many times summarized as using "coroutines". It is comparable to the main key feature of Go, the "Goroutines".

#### Concurrency and Burgers¶

This idea of asynchronous code described above is also sometimes called "concurrency". It is different from "parallelism".

Concurrency and parallelism both relate to "different things happening more or less at the same time".

But the details between concurrency and parallelism are quite different.

To see the difference, imagine the following story about burgers:

##### Concurrent Burgers¶

You go with your crush to get fast food, you stand in line while the cashier takes the orders from the people in front of you.
Then it's your turn, you place your order of 2 very fancy burgers for your crush and you.
The cashier says something to the cook in the kitchen so they know they have to prepare your burgers (even though they are currently preparing the ones for the previous clients).
You pay. 💸

The cashier gives you the number of your turn.
While you are waiting, you go with your crush and pick a table, you sit and talk with your crush for a long time (as your burgers are very fancy and take some time to prepare).

As you are sitting at the table with your crush, while you wait for the burgers, you can spend that time admiring how awesome, cute and smart your crush is.
While waiting and talking to your crush, from time to time, you check the number displayed on the counter to see if it's your turn already.

Then at some point, it finally is your turn. You go to the counter, get your burgers and come back to the table.
You and your crush eat the burgers and have a nice time. ✨

While you are at the line, you are just idle 😴, waiting for your turn, not doing anything very "productive". But the line is fast because the cashier is only taking the orders (not preparing them), so that's fine.

Then, when it's your turn, you do actual "productive" work, you process the menu, decide what you want, get your crush's choice, pay, check that you give the correct bill or card, check that you are charged correctly, check that the order has the correct items, etc.

But then, even though you still don't have your burgers, your work with the cashier is "on pause" ⏸, because you have to wait 🕙 for your burgers to be ready.

But as you go away from the counter and sit at the table with a number for your turn, you can switch 🔀 your attention to your crush, and "work" ⏯ 🤓 on that. Then you are again doing something very "productive" as is flirting with your crush 😍.

Then the cashier 💁 says "I'm finished with doing the burgers" by putting your number on the counter's display, but you don't jump like crazy immediately when the displayed number changes to your turn number. You know no one will steal your burgers because you have the number of your turn, and they have theirs.

So you wait for your crush to finish the story (finish the current work ⏯ / task being processed 🤓), smile gently and say that you are going for the burgers ⏸.

Then you go to the counter 🔀, to the initial task that is now finished ⏯, pick the burgers, say thanks and take them to the table. That finishes that step / task of interaction with the counter ⏹. That in turn, creates a new task, of "eating burgers" 🔀 ⏯, but the previous one of "getting burgers" is finished ⏹.

## Parallel Burgers¶

Now let's imagine these aren't "Concurrent Burgers", but "Parallel Burgers".

You go with your crush to get parallel fast food.

You stand in line while several (let's say 8) cashiers that at the same time are cooks take the orders from the people in front of you.

Everyone before you is waiting for their burgers to be ready before leaving the counter because each of the 8 cashiers goes and prepares the burger right away before getting the next order.

Then it's finally your turn, you place your order of 2 very fancy burgers for your crush and you.

You pay 💸.

The cashier goes to the kitchen.

You wait, standing in front of the counter 🕙, so that no one else takes your burgers before you do, as there are no numbers for turns.

As you and your crush are busy not letting anyone get in front of you and take your burgers whenever they arrive, you cannot pay attention to your crush. 😞

This is "synchronous" work, you are "synchronized" with the cashier/cook 👨‍🍳. You have to wait 🕙 and be there at the exact moment that the cashier/cook 👨‍🍳 finishes the burgers and gives them to you, or otherwise, someone else might take them.

Then your cashier/cook 👨‍🍳 finally comes back with your burgers, after a long time waiting 🕙 there in front of the counter.

You take your burgers and go to the table with your crush.

You just eat them, and you are done. ⏹

There was not much talk or flirting as most of the time was spent waiting 🕙 in front of the counter. 😞
In this scenario of the parallel burgers, you are a computer / program 🤖 with two processors (you and your crush), both waiting 🕙 and dedicating their attention ⏯ to be "waiting on the counter" 🕙 for a long time.

The fast food store has 8 processors (cashiers/cooks). While the concurrent burgers store might have had only 2 (one cashier and one cook).

But still, the final experience is not the best.

### conclusion

Many, many users, but your server is waiting 🕙 for their not-so-good connection to send their requests.

And then waiting 🕙 again for the responses to come back.

This "waiting" 🕙 is measured in microseconds, but still, summing it all, it's a lot of waiting in the end.

That's why it makes a lot of sense to use asynchronous ⏸🔀⏯ code for web APIs.

This kind of asynchronicity is what made NodeJS popular (even though NodeJS is not parallel) and that's the strength of Go as a programming language.

And that's the same level of performance you get with FastAPI.

And as you can have parallelism and asynchronicity at the same time, you get higher performance than most of the tested NodeJS frameworks and on par with Go, which is a compiled language closer to C

## Is concurrency better than parallelism?¶

Nope! That's not the moral of the story.

Concurrency is different than parallelism. And it is better on specific scenarios that involve a lot of waiting. Because of that, it generally is a lot better than parallelism for web application development. But not for everything.

So, to balance that out, imagine the following short story:

You have to clean a big, dirty house.

Yep, that's the whole story.

# More technical details¶

You might have noticed that await can only be used inside of functions defined with `async def`

But at the same time, functions defined with `async def` have to be "awaited". So, functions with `async def` can only be called inside of functions defined with `async def` too.

######################################################################################################

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

###########################################################################

The difference between the two is the way the response model is specified.

### `@app.get("/api/todo{title}", response_model=baseTodoClass)`

In this syntax, the response_model parameter is explicitly specified as part of the @app.get decorator. This tells FastAPI to use the baseTodoClass class as the response model for this endpoint.

### `@app.get("/api/todo{title}") -> baseTodoClass`

In this syntax, the response model is specified using the `->` syntax, which is a shorthand way to specify the response model. This is equivalent to the first syntax, but is a more concise way to specify the response model.
Both syntaxes achieve the same result, which is to specify the response model for the endpoint. However, the first syntax is more explicit and clear, while the second syntax is more concise and shorthand.
