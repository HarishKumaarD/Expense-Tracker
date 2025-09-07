# 💰 Personal Expense Tracker API

A comprehensive FastAPI-based REST API for managing personal expenses, budgets, and financial analytics. Built with modern Python technologies and best practices.

## 🚀 Features

- **User Authentication** - JWT-based secure authentication
- **Expense Management** - Create, read, update, delete expenses
- **Budget Tracking** - Set and monitor spending budgets
- **Analytics & Reporting** - Spending summaries and category analysis
- **RESTful API** - Clean, documented API endpoints
- **Real-time Data** - Instant expense tracking and budget monitoring

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for Python
- **SQLAlchemy** - SQL toolkit and ORM
- **JWT Authentication** - Secure token-based authentication
- **Pydantic** - Data validation using Python type hints
- **Uvicorn** - ASGI server for production
- **Python 3.8+** - Modern Python features

## 📁 Project Structure

```
expense-tracker/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── security.py          # Authentication & JWT
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Authentication endpoints
│       ├── expenses.py      # Expense management
│       ├── budgets.py       # Budget management
│       └── analytics.py     # Analytics endpoints
├── .env                     # Environment variables (not in repo)
├── .gitignore
├── run.py                   # Server startup script
├── requirements.txt         # Python dependencies
└── README.md
```

## 🚦 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/expense-tracker.git
   cd expense-tracker
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   .\venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, visit:
- **Interactive Docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🔧 Configuration

Create a `.env` file in the project root with the following variables:

```bash
# JWT Configuration
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Server Configuration
HOST=0.0.0.0
PORT=8000

# CORS Configuration
ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Environment
ENVIRONMENT=development
```

## 🧪 API Testing

### Using Postman
1. Import the Postman collection from `postman/` directory
2. Set up the environment variables
3. Run the test collection

### Using curl
```bash
# Health check
curl -X GET "http://localhost:8000/health"

# Register user
curl -X POST "http://localhost:8000/api/auth/register" \
     -H "Content-Type: application/json" \
     -d '{"email":"user@example.com","password":"password123","full_name":"Test User"}'

# Login
curl -X POST "http://localhost:8000/api/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=user@example.com&password=password123"
```

## 📊 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user profile

### Expenses
- `GET /api/expenses/` - List all expenses
- `POST /api/expenses/` - Create new expense
- `GET /api/expenses/{id}` - Get expense by ID
- `PUT /api/expenses/{id}` - Update expense
- `DELETE /api/expenses/{id}` - Delete expense

### Budgets
- `GET /api/budgets/` - List all budgets
- `POST /api/budgets/` - Create new budget
- `GET /api/budgets/{id}` - Get budget by ID
- `PUT /api/budgets/{id}` - Update budget
- `DELETE /api/budgets/{id}` - Delete budget

### Analytics
- `GET /api/analytics/summary` - Get spending summary
- `GET /api/analytics/by-category` - Get expenses by category
- `GET /api/analytics/monthly-trends` - Get monthly spending trends

## 🧪 Testing

Run the included test script:
```bash
python test_api.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚀 Deployment

### Using Docker (Coming Soon)
```bash
docker build -t expense-tracker .
docker run -p 8000:8000 expense-tracker
```

### Using Cloud Platforms
- **Heroku**: See `Procfile` for deployment configuration
- **Railway**: Direct deployment from GitHub
- **DigitalOcean App Platform**: One-click deployment

## 🛡️ Security

- JWT tokens for secure authentication
- Password hashing with bcrypt
- Environment-based configuration
- CORS protection configured
- Input validation with Pydantic

## 📞 Support

If you have any questions or issues, please:
1. Check the [API Documentation](http://localhost:8000/docs)
2. Look through existing [Issues](https://github.com/YOUR_USERNAME/expense-tracker/issues)
3. Create a new issue if needed

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The amazing web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL toolkit
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation library

---

**Built with ❤️ using FastAPI**
