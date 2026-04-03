# Task 1: Build and Run a Dockerized Flask Application 

## How to Dockerize a Simple Python Flask Application

<p>This project demonstrates how to containerize a basic Python Flask application using Docker.
The goal is to understand how Docker images are built and how containers run applications in isolation.</p>

<h2>Project Overview</h2>
<p>We will:</p>
<ul>
  <li>Create a simple Flask web application</li>
  <li>Write a Dockerfile</li>
  <li>Build a Docker image</li>
  <li>Run the container</li>
  <li>Access the application in the browser</li>
</ul>

<h2>Prerequisites</h2>
<p>Before starting, make sure the following are installed:</p>
<ul>
  <li>Docker</li>
  <li>Git (optional, for version control)</li>
</ul>

<p>Verify Docker installation:</p>
<pre><code>docker --version</code></pre>
<p>You should see a Docker version installed.</p>

<h2>Step 1: Create Project Directory</h2>
<p>Create a new folder and move into it:</p>
<pre><code>mkdir docker-python-app
cd docker-python-app</code></pre>

<h2>Step 2: Create the Flask Application</h2>
<p>Create a file named <b>app.py</b>:</p>
<pre><code>nano app.py</code></pre>

<p>Add the following content:</p>

**Flask Application Code:**

   - Create a Python file `app.py` with the following code:
     ```python
     from flask import Flask
     app = Flask(__name__)

     @app.route('/')
     def home():
         return "Welcome to Dockerized Flask Application!"

     if __name__ == "__main__":
         app.run(host="0.0.0.0", port=5000)
     ```

<p>This creates a simple API that returns a JSON response.</p>

<h2>Step 3: Create Requirements File</h2>
<p>Create a file named <b>requirements.txt</b>:</p>
<pre><code>nano requirements.txt</code></pre>

<p>Add:</p>
<pre><code>flask</code></pre>

<p>This file tells Docker which Python dependencies to install.</p>

<h2>Step 4: Create the Dockerfile</h2>
<p>Create a file named <b>Dockerfile</b>:</p>
<pre><code>nano Dockerfile</code></pre>

<p>Add the following content:</p>

   - Write a `Dockerfile` to containerize the Flask application:
     ```Dockerfile
     # Use the official Python image as a base
     FROM python:3.9-slim

     # Set the working directory in the container
     WORKDIR /app

     # Copy the current directory contents into the container
     COPY . /app

     # Install Flask
     RUN pip install flask

     # Expose the application on port 5000
     EXPOSE 5000

     # Command to run the application
     CMD ["python", "app.py"]
     ```

<h3>Explanation:</h3>
<ul>
  <li><b>FROM</b> defines the base image</li>
  <li><b>WORKDIR</b> sets the working directory inside the container</li>
  <li><b>COPY</b> moves files into the container</li>
  <li><b>RUN</b> installs dependencies</li>
  <li><b>EXPOSE</b> documents the port</li>
  <li><b>CMD</b> starts the application</li>
</ul>

<h2>Step 5: Verify Project Structure</h2>
<p>Your folder should look like this:</p>
<pre><code>docker-python-app/
├── app.py
├── requirements.txt
└── Dockerfile</code></pre>

<h2>Step 6: Build Docker Image</h2>
<p>Run the following command inside the project directory:</p>
<pre><code>docker build -t python-flask-app .</code></pre>

<p>Check if the image was created:</p>
<pre><code>docker images</code></pre>

<p>You should see <b>python-flask-app</b> listed.</p>

<h2>Step 7: Run the Container</h2>
<p>Start the container:</p>
<pre><code>docker run -d -p 5000:5000 --name flask-container python-flask-app</code></pre>

<p>Verify it is running:</p>
<pre><code>docker ps</code></pre>

<h2>Step 8: Access the Application</h2>
<p>Open your browser and visit:</p>
<pre><code>http://localhost:5000</code></pre>

<p>You should see:</p>
<pre><code>{"message": "Welcome to Dockerized Flask Application!"}</code></pre>

<h2>Step 9: Useful Docker Commands</h2>

<p><b>View logs:</b></p>
<pre><code>docker logs flask-container</code></pre>

<p><b>Access container shell:</b></p>
<pre><code>docker exec -it flask-container sh</code></pre>

<p><b>Stop container:</b></p>
<pre><code>docker stop flask-container</code></pre>

<p><b>Remove container:</b></p>
<pre><code>docker rm flask-container</code></pre>

<p><b>Remove image:</b></p>
<pre><code>docker rmi python-flask-app</code></pre>
