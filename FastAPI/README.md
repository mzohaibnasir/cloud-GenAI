# FastAPI

is a modern high performance, web framework for building APIs with python. It uses ASGI(Asychronous Server Gateway Interface)
whereas Flask/Django uses WSGI(Web server Gateway Interface).

# ASGI is intended to provide a standard interface between asyc-capable python web servers, frameworks and applications.

1.  WSGI provided a standard for synchronous pytohn apps, ASGI provides one for both asynchronous and synchronous apps with a WSGI backwards-capability implementation and multiple servers and application frameworks. WSGi is used by Flask and Django

2.  WSGI - sychronous; ASGI - asynchronous

## Pydantic is the most widely used data validation library for Python.

############################################

SGI and ASGI are both interfaces that act as middlemen between web servers and Python web applications. They define how data is exchanged between these two components. Here's a breakdown of their key differences:

## Processing Style:

WSGI (Web Server Gateway Interface): WSGI uses synchronous processing. This means the web server handles requests one at a time. A worker thread gets tied up waiting for slow tasks like database calls to finish before moving on to the next request.

ASGI (Asynchronous Server Gateway Interface): ASGI is built for asynchronous programming. This allows the web server to handle multiple requests concurrently. Even if one request is waiting on a slow task, the server can handle others without being blocked.

## Use Cases:

WSGI: A good choice for simpler applications with moderate traffic that don't require fancy features like WebSockets or real-time communication. WSGI frameworks like Django and Flask are well-established and have a vast ecosystem of libraries.

ASGI: Ideal for complex, high-traffic applications that benefit from handling many requests simultaneously. ASGI shines in applications using WebSockets or real-time features. Frameworks like Starlette and Sanic are built for ASGI.

## Compatibility:

WSGI: WSGI has been around for longer and is widely supported by most web servers and hosting environments.

ASGI: ASGI is a newer specification. You might need to use specific web servers like Daphne or uvicorn for ASGI applications.

In summary, WSGI is the traditional way of running Python web applications, while ASGI offers a more performant approach for modern web development needs. The choice between them depends on the complexity and requirements of your application.
