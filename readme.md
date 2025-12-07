# Web application with Python and Flask

A Flask-based web application that allows users to create accounts, log in securely, and manage their personal movie collections. Users can add movies with custom rankings, view their collection, and delete entries as needed.

## Features

- **User Authentication**: Secure registration and login with bcrypt password hashing
- **Personal Movie Lists**: Each user maintains their own collection of movies
- **CRUD Operations**: Create, read, and delete movies from your collection
- **Session Management**: Secure session handling for user state
- **Responsive UI**: Clean, gradient-styled interface with modern CSS

## Technologies & Concepts

During this project, I was able to demonstrate several key Python and web development concepts:

### Object-Oriented Programming (OOP)
- **Models**: [`User`](models/user.py), [`Movie`](models/movie.py), and [`UserMovies`](models/user_movies.py) represent database entities using SQLAlchemy ORM
- **Services**: Business logic abstraction in [`MovieService`](services/movie_service.py), [`UserService`](services/user_service.py), and [`UserMoviesService`](services/user_movies_service.py)
- **Repositories**: Data access layer pattern in [`MovieRepository`](repositories/movie_repository.py), [`UserRepository`](repositories/user_repository.py), and [`UserMoviesRepository`](repositories/user_movies_repository.py)

### Security
- **Password Hashing**: bcrypt implementation in [`HashingService`](services/hashing_service.py) for secure password storage
- **Session Management**: Flask sessions for maintaining authenticated user state
- **Environment Variables**: Sensitive configuration stored in `.env` file (database URI, secret keys)

### Flask Framework
- **Routing**: RESTful endpoints defined in controllers ([`page_controller.py`](controllers/page_controller.py), [`login_controller.py`](controllers/login_controller.py), [`user_controller.py`](controllers/user_controller.py), [`movie_controller.py`](controllers/movie_controller.py))
- **Templates**: Jinja2 templating for dynamic HTML rendering
- **Static Files**: CSS styling in [`static/style/style.css`](static/style/style.css)
- **Flash Messages**: User feedback for login errors and account creation

### Database
- **SQLAlchemy ORM**: Database abstraction layer
- **MySQL**: Backend database (configurable via environment variables)
- **Relationships**: Many-to-many relationship between users and movies through the `user_movies` junction table

## Prerequisites to run the app

- Python 3.10+
- MySQL server running locally
- pip (Python package manager)

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd my-top-movies
   ```

2. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy pymysql python-dotenv bcrypt
   ```

3. **Configure environment variables**
   
   Create a `.env` file in the root directory and add the following variables:
   ```env
   DATABASE_URI=mysql+pymysql://root:your_password@localhost:3306/my_top_movies
   APP_SECRET_KEY=your_secret_key_here
   ```

4. **Set up the database**
   
   Create a MySQL database named `my_top_movies`:
   ```sql
   CREATE DATABASE my_top_movies;
   ```

5. **Run the application**
   ```bash
   python main.py
   or
   python3 main.py
   ```

   The app will be available at `http://127.0.0.1:5000`

## Project Structure

```
├── main.py                    # Application entry point
├── db.py                      # Database initialization
├── controllers/               # Route handlers
│   ├── login_controller.py
│   ├── movie_controller.py
│   ├── page_controller.py
│   └── user_controller.py
├── services/                  # Business logic layer
│   ├── hashing_service.py
│   ├── movie_service.py
│   ├── user_movies_service.py
│   └── user_service.py
├── repositories/              # Data access layer
│   ├── movie_repository.py
│   ├── user_movies_repository.py
│   └── user_repository.py
├── models/                    # SQLAlchemy models
│   ├── movie.py
│   ├── user.py
│   └── user_movies.py
├── templates/                 # HTML templates
└── static/                    # CSS and static assets
```

## Usage

1. Navigate to `/my-top-movies/login`
2. Create a new account or log in with existing credentials
3. Add movies to your collection with custom rankings (1-10)
4. View, manage, and delete movies from your personal list
5. Log out when finished

## Development Notes

- The application follows a **layered architecture** pattern (Controller → Service → Repository → Model)
- Database tables are created automatically on first run via `db.create_all()`
- Sessions are managed server-side with Flask's session middleware
- All passwords are hashed using bcrypt before storage

