# Python - Network #1

## Task 0: Basics of HTTP/HTTPS

### 1. Differences Between HTTP and HTTPS
* **HTTP (Hypertext Transfer Protocol):** 
  * Transfers data in plain text (unencrypted).
  * Vulnerable to eavesdropping and Man-in-the-Middle (MitM) attacks.
  * Operates on default port **80**.

* **HTTPS (HTTP Secure):** 
  * Encrypts communication using **SSL/TLS** encryption layers.
  * Ensures data confidentiality, integrity, and authentication.
  * Operates on default port **443**.
  * Used for sensitive transactions like banking, logins, and online payments.

---

### 2. Structure of HTTP Request and Response

#### A. HTTP Request Structure
An HTTP request sent by a client (e.g., browser or script) consists of:
1. **Request Line:** Includes the HTTP Method, Request URI, and HTTP Version (e.g., `GET /index.html HTTP/1.1`).
2. **Request Headers:** Key-value pairs providing metadata about the request (e.g., `User-Agent`, `Accept`, `Authorization`).
3. **Empty Line:** Separates the headers from the body.
4. **Message Body (Optional):** Contains data sent to the server (used in `POST`, `PUT`, `PATCH` requests).

#### B. HTTP Response Structure
An HTTP response returned by the server consists of:
1. **Status Line:** Includes HTTP Version, Status Code, and Reason Phrase (e.g., `HTTP/1.1 200 OK`).
2. **Response Headers:** Metadata about the response and server (e.g., `Content-Type`, `Content-Length`, `Set-Cookie`).
3. **Empty Line:** Separates headers from the body.
4. **Message Body:** The requested resource or data (e.g., HTML content, JSON object).

---

### 3. Common HTTP Methods
1. **GET:**
   * **Description:** Retrieves data from a specified resource without altering server state.
   * **Use Case:** Fetching a web page or getting data from an API.
2. **POST:**
   * **Description:** Sends data to the server to create a new resource.
   * **Use Case:** Submitting a form or uploading a file.
3. **PUT:**
   * **Description:** Replaces or updates an existing resource entirely with the request payload.
   * **Use Case:** Updating user profile details on a server.
4. **DELETE:**
   * **Description:** Removes a specified resource from the server.
   * **Use Case:** Deleting a user account or an item from a list.

---

### 4. Common HTTP Status Codes
1. **200 OK:**
   * **Description:** Successful request.
   * **Scenario:** Successfully loading a web page.
2. **301 Moved Permanently:**
   * **Description:** The requested URL has been permanently moved.
   * **Scenario:** Redirecting HTTP traffic to HTTPS.
3. **400 Bad Request:**
   * **Description:** The server cannot process the request due to invalid syntax.
   * **Scenario:** Sending an invalid JSON payload in a request.
4. **404 Not Found:**
   * **Description:** The requested resource isn't available on the server.
   * **Scenario:** Navigating to a non-existent URL page.
5. **500 Internal Server Error:**
   * **Description:** The server encountered an unexpected error.
   * **Scenario:** An unhandled exception or crash in the server backend code.
