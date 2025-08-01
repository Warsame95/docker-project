# Flask + Redis Visit Counter App

## 📌 Project Overview

This is a simple multi-container web application that tracks the number of visits to a page. It is built using **Flask** for the backend, **Redis** as an in-memory data store, and **NGINX** as a load balancer to distribute traffic across multiple Flask instances.

Each time a user visits the `/count` route, their visit is recorded in Redis, and the updated count is displayed. The app demonstrates containerized service interaction using Docker and Docker Compose.

---

## 🧠 What This Project Does

- 🌐 Displays a **welcome page** with a button to view the visit count.
- 🔁 Tracks how many times the `/count` page has been visited.
- 📊 Stores and updates the count using **Redis**.
- 🔀 Scales the Flask application using **Docker Compose**.
- ⚖️ Uses **NGINX** as a load balancer to route requests between multiple Flask containers.

---

## 🧰 Technologies & Concepts Learned

- **Flask** – Creating web routes and rendering HTML templates.
- **Redis** – Storing and incrementing page visit counts.
- **Docker** – Containerizing Flask apps and Redis.
- **Docker Compose** – Running multi-container applications.
- **NGINX** – Acting as a reverse proxy and load balancer.

---
<img width="1434" height="683" alt="Screenshot 2025-08-01 at 16 11 45" src="https://github.com/user-attachments/assets/8ce9f350-adf7-46ae-866a-dd7247bd80b3" />

<img width="1434" height="680" alt="Screenshot 2025-08-01 at 16 12 05" src="https://github.com/user-attachments/assets/b8eb92a0-407f-4cba-a496-804c2959e54b" />

---
## 🧱 Prerequisites

Before you start, make sure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/) (comes bundled with Docker Desktop)

---

## 🚀 How to Run This App

1. **Clone the repository**
2. **Navigate into the project folder**
3. **Run the app using:**

```bash
docker-compose up --build


