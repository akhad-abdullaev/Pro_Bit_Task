
# 🌊 Test Task

Hydro is a scalable and modular backend system for managing operations, developed using **Django**, **PostgreSQL**, and **Docker**. It supports both production and development environments with clean code enforcement via `flake8`.

---

## 🚀 Features

- Modular Django backend architecture
- PostgreSQL database integration
- Dockerized environment with `docker-compose`
- Code quality enforcement with **flake8**
- Environment separation: `production` and `devmode`
- OAuth2 / JWT authentication ready

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/4sqdep/forma.git
cd forma
```

### 2. Set up environment variables

Copy the example env file and update values:

```bash
cp .env.example .env
```

### 3. Start services

#### Production:
```bash
docker compose up -d --build
```

---

## 🧪 Linting with Flake8

To run `flake8` in Docker:

```bash
docker compose -f devmode.yml run --rm flake8
```

You can also configure it in `devmode.yml` like this:

```yaml
  flake8:
    image: python:3.11
    volumes:
      - .:/code
    working_dir: /code
    command: bash -c "pip install flake8 && flake8 ."
```

---

## 🛠 Usage

Access the API:

- **Development**: `http://localhost:8000`

Admin panel: `http://<your-domain>/admin/`

---

## 🧰 Tech Stack

- **Backend**: Django / DRF
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose
- **Auth**: JWT / OAuth2
- **Linting**: Flake8

---

## 👥 Contributing

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Merge Request

---

## 🛡 License

This project is licensed under the MIT License.

---

## 📈 Project Status

✅ Actively maintained & open to contributions