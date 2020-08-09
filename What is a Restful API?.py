#API notes from What is a RESTful API? Explanation of REST & HTTP
# https://www.youtube.com/watch?v=Q-BpqyOT3a8&feature=youtu.be&fbclid=IwAR1gVV0CO4iFg7vp-oKR771x61hPQ6z8yr5SSkJdXg3WY3ZA0gr-60hxNJw

#API - Application Program Interface
# It is a contract from one software to another in a structured request and response

"""
Analogy 1

Resturant

Web app (client)
Server  (API)  - structured to take orders and bring order back which will the data or response
                a messenger or a waiter running software

REST
REST - Representation State Transfer
    - It is an architecture style for designing networked applications
    - It relies on a stateless, client-server protocol, almost always HTTP
    - treats server objects as resources that can be created or destroyed
    - Can be used by virtually any programming language

HTTP Methods

GET: Retrieve data from a specified resource like a browser client going to a specific server URI
POST: Submit data to be processed to a specified resource
PUT: Update a specified resource - is sending a request to an endpoint which is a URI
Delete: Delete a specified resource

HEAD : Same as GET but does not return the body
OPTIONS: Returns the supported HTTP methods
PATCH: Update partial resources

Endpoints

THE URI/URL where api/service can be accessed by a client application


Authentication
Some API's require authentication to use their service. This could be free or paid.
OAUTh - is a type of access token to be sent with a request.

https://docs.github.com/en/rest
This API has a lot of information about the github API with methods and end points.

JSON (JavaScript ObjectNotation) is a lightweight data-interchange format that is easy to read and write.

An application should be registered at REgister a new Oauth application on GitHub if the user wants there to be
many requests for that api otherwise it will retrieve an error.



"""


