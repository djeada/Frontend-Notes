# HTTP

## HTTP

Hypertext Transfer Protocol

= protocol for requesting and transferring resources over a network

## HTTP

Pair: Request - Response

Request: from the browser (mostly)

Response: from the server

HTTP requests and responses are transferred via a _lower-level_ protocol, most commonly _TCP_

## Experimenting with HTTP

via:

- Firefox tools under _network_
- VS Code Plugin _HTTP Client_

## HTTP example: Wikipedia

Request:

```http
GET /wiki/Main_Page HTTP/2.0
Host: en.wikipedia.org
Connection: keep-alive
```

Response:

```http
HTTP/2.0 200 OK
Date: Wed, 24 Apr 2019 07:50:41 GMT
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html ...
```

## HTTP example: Wikipedia search (1)

request:

```http
GET /w/index.php?search=test&title=Special:Search&go=Go HTTP/2.0
Host: en.wikipedia.org
Connection: keep-alive
```

response:

```http
HTTP/2.0 302 Found
Location: https://en.wikipedia.org/wiki/Test
Content-Length: 0
```

## HTTP example: Wikipedia search (2)

request:

```http
GET /wiki/Test HTTP/2.0
Host: en.wikipedia.org
Connection: keep-alive
```

response:

```http
HTTP/2.0 200 OK
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html ...
```

## HTTP example: POST request

request:

```http
POST /submit-posting HTTP/2.0
Host: example.com
Connection: keep-alive
Content-Type: text/plain; encoding=UTF-8
Content-Length: 33

This is the post content (body)
```

response:

```http
HTTP/2.0 200 OK
Content-Type: text/html; charset=UTF-8

...
```

## HTTP example: API

```http
GET /todos/12
Host: jsonplaceholder.typicode.com
Connection: keep-alive
```

```http
HTTP/2.0 200 OK
Content-Type: application/json; charset=utf-8
Etag: W/"5c-cn8o...

{
  "userId": 1,
  "id": 12,
  "title": "ipsa repellendus fugit nisi",
  "completed": true
}
```

## Important request header fields

- _`Host`_
- _`Connection`_
- `Origin`
- `Accept`
- `Accept-Encoding`
- `Cookie`
- `Cache-Control`
- `Dnt`

## Important HTTP status codes

- `200 OK`

<!-- list separator -->

- `301 Moved Permanently`
- `307 Temporary Redirect` (Redirect to other address)
- `303 See Other` (Redirect to other address, HTTP method changes is set to `GET`)
- `308 Permanent Redirect`
- `304 Not Modified` (Resource did not change since last query)

## Important HTTP status codes

- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`
- `404 Not Found`

<!-- list separator -->

- `500 Internal Server Error`

see also: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

## Important response header fields

- `Content-Length`
- `Content-Type`
- `Set-Cookie`
- `Location`
- `Cache-Control`

## Header field "Content-Type"

possible values:

- `text/plain; charset=utf-8`
- `text/html; charset=utf-8`
- `application/json`
- `application/javascript`
- `application/ecmascript`
- `image/jpeg`
- `image/png`
- ...

## Header field "Set-Cookie"

example:

```http
GET /
Host: www.google.com

Set-Cookie: 1P_JAR=2019-04-24-08; expires=...; path=/; domain=.google.com
Set-Cookie: IDCC=AN0-TYtU7...fo; expires=...; path=/; domain=.google.com
```

HTTP API / web API = means of transmitting data sets between a client and a web server

## HTTP APIs

standards:

- XML-RPC (1998)
- SOAP (1999)
- JSON-RPC (2005)
- REST (2000)
- GraphQL (2015)

## HTTP APIs

request format:

- SOAP: XML
- JSON-RPC: JSON
- REST: URL + HTTP method (+ URL parameters) (+ request body)
- GraphQL: GraphQL query language

response format:

- SOAP: XML
- JSON-RPC: JSON
- REST: commonly JSON (or XML, ...)
- GraphQL: JSON

## Comparison of REST, JSON-RPC and GraphQL

- fixed vs flexible queries
- fixed protocol vs protocol agnostic

## Fixed vs flexible queries

**REST**, **JSON-RPC**: _endpoints_ / _methods_ are fixed (e.g. _posts_of_friends_, _suggested_friends_, ...)

**GraphQL**: client can construct their own query in a flexible way

Advantage of GraphQL: more flexible, new functionality may not need extra code on the backend

Disadvantage of GraphQL: may often need additional code to restrict access (e.g. prevent querying for _posts of suggested friends_)

## Fixed protocol vs protocol agnostic

**REST** is commonly associated with HTTP, distinguishing API calls by their HTTP methods (_get_, _post_, ...)

**JSON-RPC** and **GraphQL** could be used with other protocols, e.g. WebSockets

## JSON-RPC

RPC = remote procedure call

## JSON-RPC

example request body:

```json
{
  "jsonrpc": "2.0",
  "method": "get_todo_by_id",
  "params": { "id": 1 },
  "id": 1234
}
```

example response body:

```json
{
  "jsonrpc": "2.0",
  "error": null,
  "result": [
    { "id": 1, "title": "groceries", "completed": false }
  ],
  "id": 1234
}
```

## REST

REST = Representational State Transfer

Mostly via HTTP requests with these methods:

- querying elements via `GET`
- adding an element via `POST`
- adding an element at a specific URL via `PUT`
- modifying an element via `PATCH`
- replacing an element via `PUT`
- deleting an element via `DELETE`
- any other modification via `POST`

## REST examples

_get_: querying multiple entries:

```http
GET /todos HTTP/2.0
Host: jsonplaceholder.typicode.com
```

_get_: querying a single entity:

```http
GET /todos/2 HTTP/2.0
Host: jsonplaceholder.typicode.com
```

_get_: querying three entities by identifier:

```http
GET /rest/v2/alpha?codes=de;fr;it HTTP/2.0
Host: restcountries.eu
```

## REST examples

_post_: adding an entry:

```http
POST /todos HTTP/2.0
Host: jsonplaceholder.typicode.com
Content-Type: application/json
Content-Length: 27

{
  "title": "learn REST",
  "completed": false
}
```

## REST examples

_patch_: changing an entry:

```http
PATCH /todos/6 HTTP/2.0
Host: jsonplaceholder.typicode.com
Content-Type: application/json
Content-Length: 23

{
  "completed": true
}
```

## REST examples

_delete_: deleting an entry:

```http
DELETE /todos/6 HTTP/2.0
Host: jsonplaceholder.typicode.com
```

## REST examples

_post_: other request (deleting all completed todos):

```http
POST /todos/delete_completed HTTP/2.0
Host: ...
```

## Resources

example REST APIs:

- [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)
- [restcountries.eu](https://restcountries.eu)


# ALL CODES

Informational   1xx
Successful      2xx
Redirection     3xx
Client Error    4xx
Server Error    5xx

100 Continue
101 Switching Protocols
--------------------------------------------
102 Processing (WebDAV) (RFC 2518)
103 Checkpoint
122 Request-URI too long (Microsoft/IE7)
--------------------------------------------
200 OK
201 Created (+ etag)
202 Accepted
203 Non-Authoritative Information
204 No Content (no body)
205 Reset Content (reset view)
206 Partial Content (+ range header)
--------------------------------------------
207 Multi-Status (WebDAV) (RFC 4918)
226 IM Used (RFC 3229)
--------------------------------------------
300 Multiple Choices
301 Moved Permanently
302 Found
303 See Other (since HTTP/1.1)
304 Not Modified
305 Use Proxy (since HTTP/1.1)
306 Switch Proxy (no longer used)
307 Temporary Redirect (since HTTP/1.1)
308 Resume Incomplete
--------------------------------------------
400 Bad Request
401 Unauthorized
402 Payment Required (future)
403 Forbidden
404 Not Found
405 Method Not Allowed
406 Not Acceptable
407 Proxy Authentication Required
408 Request Timeout
409 Conflict (with the resource)
410 Gone
411 Length Required
412 Precondition Failed
413 Request Entity Too Large
414 Request-URI Too Long
415 Unsupported Media Type
416 Requested Range Not Satisfiable
417 Expectation Failed
--------------------------------------------
418 I'm a teapot (RFC 2324)
422 Unprocessable Entity (WebDAV) (RFC 4918)
423 Locked (WebDAV) (RFC 4918)
424 Failed Dependency (WebDAV) (RFC 4918)
425 Unordered Collection (RFC 3648)
426 Upgrade Required (RFC 2817)
444 No Response (Nginx)
449 Retry With (Microsoft)
450 Blocked by Windows Parental Controls (Microsoft)
499 Client Closed Request (Nginx)
--------------------------------------------
500 Internal Server Error
501 Not Implemented
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
505 HTTP Version Not Supported
--------------------------------------------
506 Variant Also Negotiates (RFC 2295)
507 Insufficient Storage (WebDAV)(RFC 4918)
509 Bandwidth Limit Exceeded (Apache)
510 Not Extended (RFC 2774)
598 Network read timeout error (Informal convention) 
599 Network connect timeout error (Informal convention)
