# Multi-Container Application with Docker Compose

## Flask + Redis using Docker Compose

This project demonstrates a multi-container architecture using Docker Compose. It connects a Flask web application to a Redis database container. 
The application tracks how many times a page has been visited and stores the counter value inside Redis.

<h1>Project 4 — Flask + Redis using Docker Compose</h1>

<p>This project demonstrates a multi-container architecture using Docker Compose. It connects a Flask web application to a Redis database container. The application tracks how many times a page has been visited and stores the counter value inside Redis.</p>

<hr>

<h2>Architecture</h2>

<p>Request flow:</p>

<pre>User → Flask App → Redis</pre>

<p>The Flask service handles HTTP requests, while Redis stores and updates the visit counter.</p>

<hr>

<h2>Project Goal</h2>

<p>When you open:</p>

<pre>http://localhost:5000</pre>

<p>You should see a counter message that increases on each refresh:</p>

<pre>
Hello! This page has been visited 1 times.
Hello! This page has been visited 2 times.
</pre>

<p>The counter value is stored persistently inside the Redis container.</p>

<hr>

<h2>Project Structure</h2>

<pre>
docker-flask-redis/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
</pre>

<hr>

<h2>Setup Instructions</h2>

<h3>1. Create Project Folder</h3>

<pre>
mkdir docker-flask-redis
cd docker-flask-redis
</pre>

<h3>2. Install Dependencies</h3>

<p>Add required Python libraries inside <strong>requirements.txt</strong>:</p>

<pre>
flask
redis
</pre>

<h3>3. Run Application</h3>

<p>Start all services using Docker Compose:</p>

<pre>docker compose up --build</pre>

<p>If using older Docker versions:</p>

<pre>docker-compose up --build</pre>

<hr>

<h2>Open Application</h2>

<p>Visit:</p>

<pre>http://localhost:5000</pre>

<p>Refresh the page multiple times to see the visit counter increase.</p>

<hr>

<h2>Useful Commands</h2>

<h4>Stop Containers</h4>

<pre>docker compose down</pre>

<h4>View Running Services</h4>

<pre>docker compose ps</pre>

<h4>View Logs</h4>

<pre>docker compose logs</pre>

<hr>

<h2>Concepts Demonstrated</h2>

<table border="1" cellpadding="8" cellspacing="0">
<tr>
<th>Concept</th>
<th>Description</th>
</tr>
<tr>
<td>Docker Compose</td>
<td>Manages multiple containers as one application</td>
</tr>
<tr>
<td>Service Networking</td>
<td>Services communicate using service names as hostnames</td>
</tr>
<tr>
<td>depends_on</td>
<td>Controls container startup order</td>
</tr>
<tr>
<td>Environment Variables</td>
<td>Used for runtime configuration</td>
</tr>
<tr>
<td>Microservices Pattern</td>
<td>Separates application logic and database services</td>
</tr>
</table>

<hr>

<h2>Important Networking Concept</h2>

<p>The Flask application connects to Redis using the hostname <strong>redis</strong>.</p>

<p>This works because Docker Compose automatically creates a shared network where each service name becomes a DNS hostname accessible by other containers.</p>

<p>This is the same principle used in real production container environments.</p>

<hr>

<h2>Summary</h2>

<p>This project introduces real-world container orchestration concepts including multi-service applications, internal container networking, and service dependency management. It serves as a foundation for learning scalable microservice architectures and production-grade DevOps workflows.</p>

