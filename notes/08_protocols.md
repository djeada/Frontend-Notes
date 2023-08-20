## Protocols

Grasping the intricacies of network protocols is pivotal for frontend developers. This ensures seamless interaction between the frontend and backend, facilitating data requests and transfers.

## Foundational Concepts

### Internet

The Internet, often referred to as the "net," is an expansive ensemble of globally connected computers. These systems communicate using an agreed-upon set of protocols, forming the backbone of our modern digital age.

### Browsers

Web browsers act as the gateway between users and the vast universe of the Internet. They are software applications tailored to fetch, present, and traverse online content. Modern browsers, like Google Chrome, Mozilla Firefox, and Microsoft Edge, also come equipped with tools to aid developers in debugging and optimization.

### DNS (Domain Name System)

The DNS is akin to the Internet's phonebook. Instead of flipping pages to find phone numbers, the DNS system converts domain names (like `openai.com`) into IP addresses (like `192.0.2.1`). This conversion is crucial because, while domain names are easy for people to remember, computers or networks access locations based on IP addresses.

### Domain Name

A domain name is the friendly face of an IP address. Instead of remembering a string of numbers, users can type in a human-readable address, like `google.com`, to access a website. Domain names are hierarchical, with the main domain (e.g., `google`) and a domain suffix or Top-Level Domain (TLD) like `.com`.

## Diving Deeper: Protocols in Action

### HTTP/HTTPS

**HTTP (HyperText Transfer Protocol)** and its secure variant, **HTTPS**, are the primary protocols used for transferring web content. When you visit a website, your browser sends an HTTP request to the server, which then responds with the content.

- **HTTPS** (Secure) uses SSL/TLS encryption to ensure that the data transferred between the server and the browser remains confidential and untampered.

### FTP

**FTP (File Transfer Protocol)** is an older protocol used to transfer files between a client and a server. While less common in modern frontend tasks, it's still vital for certain web maintenance activities.

### WebSockets

**WebSockets** provide full-duplex communication channels over a single TCP connection. This means data can be sent simultaneously in both directions. For frontend developers, WebSockets can be invaluable for creating real-time web applications like chat apps or live sports updates.

### TCP and UDP

**TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** are foundational communication protocols. While TCP is connection-oriented and ensures data delivery, UDP is connectionless and does not guarantee data delivery, making it faster in certain applications.

## Web Security Essentials

Web security is paramount in safeguarding both websites and their users from malicious threats. Below is a dive into some core elements of web security.

### HTTPS

**HTTPS** (Hypertext Transfer Protocol Secure) is a fortified version of HTTP. It introduces encryption to the data transfer process between browsers and web servers, ensuring data integrity and confidentiality.

### CORS

**Cross-Origin Resource Sharing (CORS)** is a mechanism employing HTTP headers. It empowers servers to define which origins (specified by domain, scheme, or port) can access its resources, thus preventing unauthorized cross-origin data access.

### Content Security Policy

**Content Security Policy (CSP)** serves as a protective shield against code injection attacks, including cross-site scripting and clickjacking. It defines content sources permitted to be loaded on a web page, giving developers tighter control.

### OWASP Security Risks

**OWASP** (Open Web Application Security Project) is a collaborative platform offering a plethora of resources related to web app security. Notably, its Top Ten Project spotlights the most perilous security threats web applications face.

### Generate a CSR on Your Server

To initiate a Certificate Signing Request (CSR), leverage the OpenSSL command for servers like Apache or Nginx:

```bash
openssl req -new -newkey rsa:2048 -nodes -keyout your_domain.com.key -out your_domain.com.csr
```

### Understanding SSL/TLS

- **SSL** (Secure Sockets Layer) and its modern successor, **TLS** (Transport Layer Security), are cryptographic standards enhancing web connection security through encryption.
- Without **SSL/TLS**, servers transmit unencrypted data, leaving it susceptible to interception. SSL/TLS creates a secure conduit for data transmission, where the server's authenticity is verified by a Certificate Authority (CA).

### Acquiring an SSL/TLS Certificate

Acquire **SSL/TLS** certificates from several trusted vendors, such as:

- Namecheap
- DigiCert
- Let's Encrypt (A free alternative)

To assess if a site employs SSL/TLS, utilize tools like SSL Labs SSL Test.

### Setting Up Certificate on Your Server

To implement **SSL/TLS**:

1. Adjust your Virtual Host configuration for it to listen on port 443 (representing HTTPS) as opposed to port 80 (HTTP).
2. Indicate your SSL/TLS key and certificate file locations within your server configuration.
3. Activate SSL/TLS in your server settings.
4. Reboot the server, applying the modifications and ushering in HTTPS support for your website.

## HTTP

The protocol responsible for requesting and sending resources over the internet is HTTP.

It works with pairs of requests and responses.

- Request: comes from the browser (request method, http headers, body)
- Response: is sent from the server (status code, http headers, body)

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

- XML-RPC (1998)
- SOAP (1999)
- REST (2000)
- JSON-RPC (2005)
- GraphQL (2015)

## REST standard

REST states for Representational State Transfer.

Mostly done via HTTP methods.

Example REST APIs:

- https://jsonplaceholder.typicode.com
- https://restcountries.eu

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
| 100 | Continue |
| 101 | Switching Protocols |
| 102 | Processing (WebDAV) (RFC 2518) |
| 103 | Checkpoint |
| 122 | Request-URI too long (Microsoft/IE7) |
| ... | ... |
| 200 | OK |
| 201 | Created (+ etag) |
| 202 | Accepted |
| 203 | Non-Authoritative Information |
| 204 | No Content (no body) |
| 205 | Reset Content (reset view) |
| 206 | Partial Content (+ range header) |
| ... | ... |
| 207 | Multi-Status (WebDAV) (RFC 4918) |
| 226 | IM Used (RFC 3229) |
| ... | ... |
| 300 | Multiple Choices |
| 301 | Moved Permanently |
| 302 | Found |
| 303 | See Other (since HTTP/1.1) |
| 304 | Not Modified |
| 305 | Use Proxy (since HTTP/1.1) |
| 306 | Switch Proxy (no longer used) |
| 307 | Temporary Redirect (since HTTP/1.1) |
| 308 | Resume Incomplete |
| ... | ... |
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
| 418 | I'm a teapot (RFC 2324) |
| ... | ... |
| 422 | Unprocessable Entity (WebDAV) (RFC 4918) |
| 423 | Locked (WebDAV) (RFC 4918) |
| 424 | Failed Dependency (WebDAV) (RFC 4918) |
| 425 | Unordered Collection (RFC 3648) |
| 426 | Upgrade Required (RFC 2817) |
| 444 | No Response (Nginx) |
| 449 | Retry With (Microsoft) |
| 450 | Blocked by Windows Parental Controls (Microsoft) |
| ... | ... |
| 499 | | Client Closed Request (Nginx) |
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

When you enter a URL into a browser's address bar, a series of complex actions take place to fetch and display the desired webpage. Let's delve deeper into this process.

1. **Entering the URL**

- Upon typing `https://example-website.com`, you're not directly communicating with the website but with its associated IP address.
- IP addresses identify servers hosting website data. To initiate communication, this IP address is essential.
- The translation from domain name to IP address is done by the Domain Name System (DNS).

2. **DNS Resolution**

- The browser queries DNS servers to translate the URL into its corresponding IP address.
- If the local DNS cache (on your machine or router) doesn't have the address saved, the request goes to higher-tier DNS servers.
- Once the IP address is located, it's relayed back to the browser, sometimes being cached for faster future access.

3. **Establishing a TCP Connection**

- The browser and server establish a Transmission Control Protocol (TCP) handshake to ensure reliable data transfer.
- Data packets traverse intricate networks, passing through routers, ISPs, and many intermediary devices.
- Given the potential inefficiencies of this process, many websites use Content Delivery Networks (CDNs). CDNs store cached versions of web content in various locations, ensuring faster delivery by serving the data from a location near the user.

4. **Sending HTTP Requests**

- Post the TCP handshake, the browser sends an HTTP or HTTPS request to the server.
- This request encapsulates a request line, headers (containing metadata about the request), and occasionally, content.
- It's imperative that the request carries all necessary details for the server to understand and fulfill it.

5. **Receiving HTTP Responses**

- The server processes the request and returns an HTTP response to the browser.
- This response contains essential resources for displaying the website: HTML files, stylesheets (CSS), scripts (JavaScript), images, and more.

6. **Rendering the Webpage**

- The browser parses the server's response.
- It constructs the Document Object Model (DOM) and Cascading Style Sheets Object Model (CSSOM) trees, then combines them to render the webpage.
- Browsers might interpret and display content slightly differently based on their design and the technologies they support. Hence, while the core content remains consistent, subtle variations can be observed across different browsers.
