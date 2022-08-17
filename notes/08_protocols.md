## Table of Contents
<!--ts-->

  - [Protocols](#Protocols)
  - [Basics](#Basics)
    - [Internet](#Internet)
    - [Browsers](#Browsers)
    - [DNS](#DNS)
    - [Domain-Name](#Domain-Name)
  - [Web-Security](#Web-Security)
    - [HTTPS](#HTTPS)
    - [CORS](#CORS)
    - [Content-Security-Policy](#Content-Security-Policy)
    - [OWASP-Security-Risks](#OWASP-Security-Risks)
  - [HTTP](#HTTP)
  - [GET](#GET)
  - [POST](#POST)
  - [HTTP-APIs](#HTTP-APIs)
  - [REST-standard](#REST-standard)
  - [HTTP-response-codes](#HTTP-response-codes)

<!--te-->

## Protocols

Frontend engineers may not place as much emphasis on this area as others, but understanding of the subject is still necessary. You don't need to know every detail about how the backend works, but you do need to understand how to get data from it and how it is sent.

## Basics

### Internet

The Internet is a global network of computers connected to each other which communicate through a standardized set of protocols.

### Browsers

A web browser is a software application that enables a user to access and display web pages or other online content through its graphical user interface. 

### DNS

The Domain Name System (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load Internet resources.

### Domain Name

A domain name is a unique, easy-to-remember address used to access websites, such as ‘google.com’, and ‘facebook.com’. Users can connect to websites using domain names thanks to the DNS system.

## Web Security

### HTTPS

HTTPS is a secure way to send data between a web server and a browser.

### CORS

Cross-Origin Resource Sharing (CORS) is an HTTP-header based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.

### Content Security Policy

Content Security Policy is a computer security standard introduced to prevent cross-site scripting, clickjacking and other code injection attacks resulting from execution of malicious content in the trusted web page context.

### OWASP Security Risks

OWASP or Open Web Application Security Project is an online community that produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security.

## HTTP

The protocol responsible for requesting and sending resources over the internet is HTTP.

It works with pairs of requests and responses.

* Request: comes from the browser (request method, http headers, body)
* Response: is sent from the server (status code, http headers, body)

HTTP is built on top of other protocols. In the transport layer it is mostly TCP.

HTTP methods:

| Method | Description |
| ------ | ----------- |
| `GET` | querying elements |
| `POST` | adding and modyfing an element |
| `PUT` | adding or replacing an element at a specific URL |
| `PATCH` | modifying an element |
| `DELETE` | deleting an element |

## GET

GET method requests data from server (ex. typing in google search engine).

Example in Linux:

```Bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" https://en.wikipedia.org/wiki/SOLID
```

Response should look something like this:

```
HTTP/2 200 
date: Sun, 10 Jul 2022 15:26:12 GMT
vary: Accept-Encoding,Cookie,Authorization
server: ATS/8.0.8
...
<!DOCTYPE html>
<html ...
```

## POST

POST method submits data to be processed by the server (ex. clicking submit button on bank page).

Example in Linux:

```Bash
curl -X POST -F "q=cat" https://duckduckgo.com/
```

Response should look something like this:

```
<!DOCTYPE html>
<html lang="en-US" ...>
<head>
<meta name="description" content="DuckDuckGo...
```

## HTTP APIs

Many standards:

* XML-RPC (1998)
* SOAP (1999)
* REST (2000)
* JSON-RPC (2005)
* GraphQL (2015)

## REST standard

REST states for Representational State Transfer.

Mostly done via HTTP methods.

Example REST APIs:

* https://jsonplaceholder.typicode.com
* https://restcountries.eu

An example with GET method:

```Bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" jsonplaceholder.typicode.com/todos/3
```

Response:

```
{
  "userId": 1,
  "id": 3,
  "title": "fugiat veniam minus",
  "completed": false
}
```

An example with POST method:

```Bash
curl --data "value_a=example & value_b=another one" jsonplaceholder.typicode.com/todos
```

Response:

```
{
  "value_a": "example",
  "value_b": "another one",
  "id": 201
}
```

## HTTP response codes

* Informational   1xx
* Successful      2xx
* Redirection     3xx
* Client Error    4xx
* Server Error    5xx

| Code | Description |
| --- | --- |
| 100 | | Continue |
| 101 | Switching Protocols |
| --- | --- |
| 102 | Processing (WebDAV) (RFC 2518) |
| 103 | Checkpoint |
| 122 | Request-URI too long (Microsoft/IE7) |
| --- | --- |
| 200 | OK |
| 201 | Created (+ etag) |
| 202 | Accepted |
| 203 | Non-Authoritative Information |
| 204 | No Content (no body) |
| 205 | Reset Content (reset view) |
| 206 | Partial Content (+ range header) |
| --- | --- |
| 207 | Multi-Status (WebDAV) (RFC 4918) |
| 226 | IM Used (RFC 3229) |
| --- | --- |
| 300 | Multiple Choices |
| 301 | Moved Permanently |
| 302 | Found |
| 303 | See Other (since HTTP/1.1) |
| 304 | Not Modified |
| 305 | Use Proxy (since HTTP/1.1) |
| 306 | Switch Proxy (no longer used) |
| 307 | Temporary Redirect (since HTTP/1.1) |
| 308 | Resume Incomplete |
| --- | --- |
| 400 | Bad Request |
| 401 | Unauthorized |
| 402 | Payment Required (future) |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 406 | Not Acceptable |
| 407 | Proxy Authentication Required |
| 408 | Request Timeout |
| 409 | Conflict (with the resource) |
| 410 | Gone |
| 411 | Length Required |
| 412 | Precondition Failed |
| 413 | Request Entity Too Large |
| 414 | Request-URI Too Long |
| 415 | Unsupported Media Type |
| 416 | Requested Range Not Satisfiable |
| 417 | Expectation Failed |
| --- | --- |
| 418 | I'm a teapot (RFC 2324) |
| 422 | Unprocessable Entity (WebDAV) (RFC 4918) |
| 423 | Locked (WebDAV) (RFC 4918) |
| 424 | Failed Dependency (WebDAV) (RFC 4918) |
| 425 | Unordered Collection (RFC 3648) |
| 426 | Upgrade Required (RFC 2817) |
| 444 | No Response (Nginx) |
| 449 | Retry With (Microsoft) |
| 450 | Blocked by Windows Parental Controls (Microsoft) |
| 499 | | Client Closed Request (Nginx) |
| --- | --- |
| 500 | Internal Server Error |
| 501 | Not Implemented |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |
| 505 | HTTP Version Not Supported |
| --- | --- |
| 506 | Variant Also Negotiates (RFC 2295) |
| 507 | Insufficient Storage (WebDAV)(RFC 4918) |
| 509 | Bandwidth Limit Exceeded (Apache) |
| 510 | Not Extended (RFC 2774) |
| 598 | Network read timeout error (Informal convention)  |
| 599 | Network connect timeout error (Informal convention) |
