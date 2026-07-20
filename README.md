# 📚 Blog API

<p align="center">
  <strong>A RESTful blogging platform API built with Flask and MongoDB.</strong><br>
  Create, manage, search and organise blog posts through a clean and lightweight backend service.
</p>

---

## 📖 Overview

Blog API is a RESTful backend application that provides all the core functionality required to power a blogging platform.

The application allows users to create, retrieve, update, delete and search blog posts while storing data in MongoDB. It was built using Flask and follows a simple separation-of-concerns architecture where route handling and database operations are kept separate.

This project was developed as part of the roadmap.sh Backend Projects collection and demonstrates practical backend development concepts including:

- REST API design
- CRUD operations
- Database integration
- Environment variable management
- Request validation
- Rate limiting
- Search functionality
- API testing with Postman

---

# ✨ Features

### Blog Post Management

- Create blog posts
- Retrieve all blog posts
- Retrieve a specific blog post by ID
- Update existing blog posts
- Delete blog posts

### Search Functionality

Search blog posts by:

- Title
- Content
- Category

Searches are case-insensitive and use MongoDB regular expressions.

### Data Persistence

All blog posts are stored in MongoDB, ensuring data remains available between application restarts.

### Timestamp Tracking

Every post contains:

- `createdAt`
- `updatedAt`

allowing changes to be tracked over time.

### Rate Limiting

Most endpoints are protected using Flask-Limiter:

```text
50 requests per hour
```

This helps prevent excessive requests and basic abuse.

---

# 🛠 Technology Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Programming language            |
| Flask         | Web framework                   |
| MongoDB       | NoSQL database                  |
| PyMongo       | MongoDB driver                  |
| Flask-Limiter | Rate limiting                   |
| python-dotenv | Environment variable management |

---

# 🏗 Architecture

The application follows a layered structure:

```text
Client
   │
   ▼
Flask Routes (app.py)
   │
   ▼
Database Service Layer (services/db.py)
   │
   ▼
MongoDB Database
```

### Why This Structure?

Separating route logic from database logic makes the code:

- Easier to maintain
- Easier to test
- Easier to expand
- More readable

The route handlers focus on:

- Receiving requests
- Validating input
- Returning HTTP responses

The service layer focuses on:

- Database operations
- Query execution
- Data retrieval
- Data updates

---

# 📂 Project Structure

```text
Blog-API/
│
├── app.py
├── services/
|   ├── app.py
│   └── db.py
│
├── requirements.txt
├── LICENSE
├── README.md
│
└── venv/
```

## File Breakdown

### app.py

Contains:

- Flask application setup
- Route definitions
- Request validation
- Rate limiting configuration
- HTTP responses

### services/db.py

Contains:

- MongoDB connection
- CRUD operations
- Search functionality
- Timestamp handling

### requirements.txt

Lists all Python dependencies required to run the project.
I just used `pip freeze > requirements.txt` to make the file.

### LICENSE

Contains the project's MIT Licence.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Sheikh-H/blog-api.git

cd blog-api
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🌍 Environment Variables

Create a `.env` file in the project root:

```env
MONGO_URI=your_mongodb_connection_string
```

Example:

```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
```

The application loads this value automatically using `python-dotenv`.

---

# 🗄 MongoDB Database

The application creates and uses:

```text
Database:
rdmpsh-blog

Collection:
blog-posts
```

Each blog post follows this structure:

```json
{
  "id": 1,
  "title": "My First Post",
  "content": "Hello World",
  "category": "Technology",
  "tags": ["python", "flask"],
  "createdAt": "2026-06-03 15:30:00",
  "updatedAt": "Null"
}
```

---

# ▶ Running the Application

Start the server:

```bash
python app.py
```

or

```bash
flask run
```

The API will be available at:

```text
http://127.0.0.1:5000
```

or

```text
localhost:5000/
```

---

# 📬 API Endpoints

---

## Create a Blog Post

### POST `/posts`

Creates a new blog post.

### Request Body

```json
{
  "title": "Learning Flask",
  "content": "Flask is a lightweight Python framework.",
  "category": "Programming",
  "tags": ["python", "flask"]
}
```

### Success Response

```json
{
  "id": 1,
  "title": "Learning Flask",
  "content": "Flask is a lightweight Python framework.",
  "category": "Programming",
  "tags": ["python", "flask"],
  "createdAt": "2026-06-03 15:30:00",
  "updatedAt": "Null"
}
```

### Status Code

```text
201 Created
```

---

## Retrieve All Posts

### GET `/posts`

Returns every blog post stored in the database.

### Browser Example

```text
localhost:5000/posts
```

### Status Code

```text
200 OK
```

---

## Search Posts

### GET `/posts?term=python`

Searches:

- Title
- Content
- Category

### Browser Example

```text
localhost:5000/posts?term=python
```

### Status Code

```text
200 OK
```

---

## Retrieve a Single Post

### GET `/posts/<id>`

Example:

```text
GET /posts/1
```

Browser:

```text
localhost:5000/posts/1
```

### Status Code

```text
200 OK
```

---

## Update a Post

### PUT `/posts/<id>`

Does support partial updates.

Example:

```json
{
  "title": "Updated Title"
}
```

Only the supplied field is modified.

Example:

```text
PUT /posts/1
```

### Success Response

```json
{
  "id": 1,
  "title": "Updated Title",
  "content": "Flask is a lightweight Python framework.",
  "category": "Programming",
  "tags": ["python", "flask"],
  "createdAt": "2026-06-03 15:30:00",
  "updatedAt": "2026-06-04 09:15:00"
}
```

### Status Code

```text
200 OK
```

---

## Delete a Post

### DELETE `/posts/<id>`

Example:

```text
DELETE /posts/1
```

### Success Status

```text
204 No Content
```

---

# 🚀 Postman Usage

Postman provides a simple way to test every endpoint.

### Create a Post

1. Select POST
2. Enter:

```text
localhost:5000/posts
```

3. Choose:

```text
Body → Raw → JSON
```

4. Paste:

```json
{
  "title": "My First Post",
  "content": "Hello World",
  "category": "Technology",
  "tags": ["python", "mongodb"]
}
```

5. Click Send

---

# 💻 cURL Examples

## Create a Post

```bash
curl -X POST localhost:5000/posts \
-H "Content-Type: application/json" \
-d '{
"title":"My First Post",
"content":"Hello World",
"category":"Technology",
"tags":["python","mongodb"]
}'
```

---

## Get All Posts

```bash
curl localhost:5000/posts
```

---

## Get a Single Post

```bash
curl localhost:5000/posts/1
```

---

## Search Posts

```bash
curl "localhost:5000/posts?term=python"
```

---

## Update a Post

```bash
curl -X PUT localhost:5000/posts/1 \
-H "Content-Type: application/json" \
-d '{
"title":"Updated Post Title"
}'
```

---

## Delete a Post

```bash
curl -X DELETE localhost:5000/posts/1
```

---

# 🔍 Function Breakdown

## Database Functions (`services/db.py`)

### add_post()

Creates a new blog post and stores it in MongoDB.

### get_post()

Retrieves a single blog post by its ID.

### get_posts()

Returns every blog post from the collection.

### update_post()

Updates one or more fields and refreshes the `updatedAt` timestamp.

### delete_post()

Removes a blog post from the database.

### search_posts()

Searches title, content and category fields using MongoDB regular expressions.

---

## Route Functions (`app.py`)

### POST `/posts`

Validates request data before creating a post.

### GET `/posts`

Returns all posts or performs a search if a term is supplied.

### GET `/posts/<id>`

Returns a single blog post.

### PUT `/posts/<id>`

Updates selected fields of a blog post.

### DELETE `/posts/<id>`

Deletes a blog post by ID.

---

# ⚠ Error Responses

Examples:

### Missing Required Fields

```json
{
  "error": "unable to add post, please use all required fields"
}
```

### Post Not Found

```json
{
  "error": "post not found"
}
```

### Invalid Update Request

```json
{
  "error": "unable to update"
}
```

---

# 🛡 Rate Limiting

Uses Flask-Limiter to restrict traffic.

Current configuration:

```text
50 requests per hour
```

Applied to:

- POST /posts
- GET /posts
- GET /posts/<id>
- DELETE /posts/<id>

This helps prevent accidental or excessive API usage.

---

# 🔮 Future Improvements

Potential enhancements include:

- User authentication
- JWT authorisation
- User accounts
- Pagination
- Sorting and filtering
- Comment system
- Categories collection
- API versioning
- Docker support
- Automated testing
- Swagger/OpenAPI documentation

---

# 🎯 Roadmap.sh Project

This project was built as part of the <a href="https://roadmap.sh/projects/blogging-platform-api" target="_blank">Blogging Platform API</a> project from roadmap.sh.

The goal was to design and implement a fully functional REST API capable of managing blog content using modern backend development practices.

---

## 📄 Licence

<p>
  This project is licensed under the <b>MIT Licence</b> — see the <a href="./LICENCE">LICENCE</a> file for details.
</p>

<pre>
MIT Licence

Copyright (c) 2026 Sheikh Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</pre>

---

## Footnote

<div align="center" style="border: 1px solid green; padding: 10px; border-radius: 5px;">
  <p>🗣️ Feel free to follow, connect, and chat!</p>
  <a class="header-badge" target="_blank" href="https://github.com/Sheikh-H"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/sheikh-hussain/"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn"></a>
  <a class="header-badge" target="_blank" href="mailto:sheikh.hussain1155@gmail.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail"></a>
  <a class="header-badge" target="_blank" href="https://sheikh-hussain.onrender.com/"><img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio"></a>
</div>

<div align="center">
  <a href="https://sheikh-hussain.onrender.com/" target="_blank">By Sheikh Hussain 💚</a>
</div>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>
