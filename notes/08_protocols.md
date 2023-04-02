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

### Generate a CSR on Your Server
You must create a CSR (Certificate Signing Request) on your server.
This is accomplished using the Open SSL command, which should be accessible by default if you are using Apache or Nginx:

    openssl req -new -newkey rsa:2048 -nodes -keyout your_domain.com.key -out your_domain.com.csr

### What is SSL?

* SSL improves the security of internet connections by encrypting them.
* When servers use plain HTTP without SSL, they deliver unencrypted data to browsers. Anyone who sniffs the data may see all the transferred data, even user credentials. 
* When using SSL, all data is sent after establishing a secure session. The server first sends its credentials. The client can then ask the central authority if the credentials are legitimate. Data is transferred only after confirmation from a central authority.

### Obtain an TLS/SSL Certificate

To put it simply, SSL (Secure Sockets Layer) is the old and TLS (Transport Layer Security) is the new, though some people refer to TLS as SSL.

You can buy a certificate from this website: https://www.namecheap.com/security/ssl-certificates/domain-validation/

This webpage checks if the given URL uses TLS or SSL:  https://www.ssllabs.com/ssltest/

### Install Certificate on Your Server

1. Change your Virtual Host to listen on port 443 (HTTPS) rather than port 80 (HTTP).
2. Specify your SSL key and certificate files. 
3. Activate SSL.
4. Restart the server. 

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

The GET method requests data from the server (e.g., typing a query in a search engine).

Example using curl in the terminal:

```Bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" "https://api.github.com/users/octocat"
```

The response should look something like this:

```
HTTP/2 200 
date: Sun, 10 Jul 2022 15:26:12 GMT
vary: Accept-Encoding,Cookie,Authorization
server: ATS/8.0.8
...
{
  "login": "octocat",
  "id": 583231,
  ...
}
```

## POST

The POST method submits data to be processed by the server (e.g., submitting a form on a web page).

Example using curl in the terminal:

```Bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpassword"}' "https://reqbin.com/echo/post/json"
```

The response should look something like this:

```html
{
  "success": "true",
  "data": {
    "username": "testuser",
    "password": "testpassword"
  }
}
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

## What happens when you enter a URL in the browser?

1. You enter `https://example-website.com` in the browser.

    * Hidden behind a user-friendly name like `https://example-website.com` is an IP address of a server that keeps the website's data.
    * In order to communicate with the server, we require that IP address.
    * We obtain the address from a service known as DNS. 

2. Browser uses DNS.

    * The browser requests that the DNS service translate a given URL to an IP address.
    * If the local DNS servers do not know the IP address, they will query the global DNS servers for it.
    * When an address is identified, it is returned to the browser.

3. TCP connection between the browser and the server.

    * TCP connection is established between the browser and the server.
    * The packets from a client browser request are routed through the router, the isp and the whole networks of devices.
    * This is an extremely circuitous and inefficient route.
    * Additionaly many websites, employ a content delivery network, or cdn, to cache static and dynamic material closer to the browser.

4. HTTP requests over the TCP connection.

    * The browser sends an http request to the server in order to obtain the page's contents.
    * The http request includes a request line, headers (or request metadata), and a content.
    * The request must include all the information that the server needs to determine what kind of data it needs to send to the client.

5. HTTP responses over the TCP connection.

    * The server sends an HTTP response to the client.
    * The response includes everything the clinet needs in order to render the website (HTML, CSS, JS and resources such as images).

6. Content rendering.

    * The browser parses the server's HTTP response.
    * The content is rendered in line with the browser's rules (not every browser supports the same set of features).
