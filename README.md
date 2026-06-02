# 🧠 PulseBlog API: Personal Blogging Platform RESTful Service

<p align="center">
  <b>A lightweight, secure RESTful API for managing personal blog posts using Flask and MongoDB.</b><br>
  Built for speed, simplicity, and clean CRUD operations.
</p>

---

## 📘 Project Overview

**PulseBlog API** is a RESTful blogging backend built in Python using Flask and MongoDB. It was developed as a solution to the Roadmap.sh project:

👉 https://roadmap.sh/projects/blogging-platform-api

The API allows users to create, read, update, delete, and search blog posts with full CRUD functionality. It is designed to be simple to integrate with tools such as Postman or any frontend application.

---

## ✨ Features

- Create new blog posts
- Retrieve all posts
- Retrieve a single post by ID
- Update one or multiple fields of a post
- Delete posts
- Search posts using a keyword (title, content, category)
- MongoDB persistence (NoSQL)
- Basic rate limiting (Flask-Limiter)
- Timestamp tracking (createdAt / updatedAt)

---

## 🧰 Tech Stack

- Python 3.8+
- Flask
- MongoDB (Atlas or local)
- PyMongo
- Flask-Limiter
- python-dotenv

---

## 📁 Project Structure

<pre>
PulseBlog/
│
├── app.py              # Flask API routes
├── services/
│   └── db.py           # Database logic (MongoDB operations)
├── .env                # Environment variables (MongoDB URI)
├── requirements.txt    # Dependencies
├── LICENSE             # MIT LICENSE
└── README.md           # Documentation
</pre>

---

## ⚙️ Setup Instructions

### 1. Clone the repository
<pre>
git clone https://github.com/yourusername/pulseblog-api.git
cd pulseblog-api
</pre>

---

### 2. Create a virtual environment

<pre>
python -m venv venv
</pre>

Activate it:

- Windows:
<pre>
venv\Scripts\activate
</pre>

- Mac/Linux:
<pre>
source venv/bin/activate
</pre>

---

### 3. Install dependencies

<pre>
pip install -r requirements.txt
</pre>

---

### 4. Set up MongoDB

This project uses **MongoDB Atlas (cloud database)**.

Steps:
1. Sign up or log in at https://www.mongodb.com/atlas
2. Create a free cluster
3. Create a database user (username + password)
4. Copy your connection string (URI)

Example `.env` file:

<pre>
MONGO_URI=mongodb+srv://username:password@cluster0.mongodb.net/
</pre>

---

### 5. Run the application

<pre>
python app.py OR flask run
</pre>

Server will run at:
<pre>
http://127.0.0.1:5000
</pre>

---

## 📬 API Usage (Postman Guide)

You can test this API using **Postman** (free tool for API testing):
https://www.postman.com/

### 1. Create a Post

**POST** `/posts`

<pre>
{
  "title": "My First Post",
  "content": "Hello world",
  "category": "Tech",
  "tags": ["python", "flask"]
}
</pre>

---

### 2. Get All Posts

**GET** `/posts`

Optional search:
<pre>
/posts?term=tech
</pre>

---

### 3. Get Single Post

**GET** `/posts/<int:_id>`

Example:
<pre>
/posts/1
</pre>

---

### 4. Update Post

**PUT** `/posts/1`

You can update one or many fields:

<pre>
{
  "title": "Updated Title"
}
</pre>

---

### 5. Delete Post

**DELETE** `/posts/1`

Returns:
- `204 No Content` if successful
- `404` if not found

---

## 🧠 Important Notes

- MongoDB URI must be added to `.env`
- IDs are auto-incremented manually
- Search is case-insensitive
- Update supports partial updates (PATCH-like behaviour via PUT)
- Postman recommended for testing

---

## 📊 Roadmap.sh Project

This project was built as part of:

👉 https://roadmap.sh/projects/blogging-platform-api

---

## 📄 Licence

MIT Licence — free to use, modify, and distribute.

---

## Footnote

<div align="center" style="border: 1px solid green; padding: 10px; border-radius: 5px;">
  <p>🗣️ Feel free to follow, connect, and chat!</p>
  <a class="header-badge" target="_blank" href="https://github.com/Sheikh-H"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub">
  </a><a class="header-badge" target="_blank" href="https://www.linkedin.com/in/sheikh-hussain/"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn">
  </a><a class="header-badge" target="_blank" href="mailto:sheikh.hussain1155@gmail.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail">
  </a><a class="header-badge" target="_blank" href="https://sheikh-h.github.io/"><img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio">
  </a>
</div>

<div align="center">
  <a href="https://www.linkedin.com/in/sheikh-hussain/" target="_blank">By Sheikh Hussain 💚</a>  
</div>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>