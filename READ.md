# ClockApp Dockerized

This project contains **two Flask microservices**:

- `clock_app`: displays the current time
- `button_app`: has a button to decrement the time via API

Both apps are containerized using Docker and run together using Docker Compose.

---

## Architecture

```
[button_app] --POST--> /update_time --> [clock_app]
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/silverdeath366/clockapp_dockerized.git
cd clockapp_dockerized
```

### 2. Run the Application

```bash
docker-compose up --build
```

### 3. Access in Your Browser

- Clock App: [http://localhost:5001](http://localhost:5001)
- Button App: [http://localhost:5002](http://localhost:5002)

---

## Folder Structure

```
clockapp_dockerized/
├── clock_app/
│   ├── app.py
│   ├── templates/
│   ├── requirements.txt
│   └── Dockerfile
├── button_app/
│   ├── app.py
│   ├── templates/
│   ├── requirements.txt
│   └── Dockerfile
└── docker-compose.yml
```

---

## Stack

- Python 3.10
- Flask
- Docker
- Docker Compose

---

## Features

- Simple UI to decrement the time
- Internal Docker network connection between services
- Clean folder structure and Dockerization
