# Telusko Trac - Product Management System

A full-stack product inventory management application built with FastAPI (backend) and React (frontend). This application allows users to perform CRUD operations on products, including creating, reading, updating, and deleting product information.

## Features

- **Product Management**: Create, read, update, and delete products
- **Real-time Search**: Filter products by ID, name, or description
- **Sortable Columns**: Sort products by ID, name, price, or quantity
- **Responsive UI**: Modern, card-based design with a clean interface
- **Database Integration**: PostgreSQL database with SQLAlchemy ORM
- **RESTful API**: FastAPI backend with automatic API documentation

## Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **PostgreSQL**: Relational database
- **Python-dotenv**: Environment variable management
- **Uvicorn**: ASGI server

### Frontend
- **React**: JavaScript library for building user interfaces
- **Axios**: HTTP client for API requests
- **CSS3**: Custom styling with modern design

## Project Structure

```
FastAPI/
├── main.py                 # FastAPI application and routes
├── models.py              # Pydantic models for request/response
├── database.py            # Database connection configuration
├── database_models.py     # SQLAlchemy ORM models
├── .env                   # Environment variables (not in git)
├── requirements.txt       # Python dependencies
├── venv/                  # Python virtual environment
└── frontend/
    ├── package.json       # Node dependencies
    ├── public/
    └── src/
        ├── App.js         # Main React component
        ├── App.css        # App styles
        ├── TaglineSection.js
        └── TaglineSection.css
```

## Prerequisites

- Python 3.8+
- Node.js 14+ and npm
- PostgreSQL database

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd FastAPI
```

### 2. Backend Setup

#### Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install Python dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-dotenv
```

#### Configure Database

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

Replace `username`, `password`, and `database_name` with your PostgreSQL credentials.

### 3. Frontend Setup

```bash
cd frontend
npm install
```

## Running the Application

### Start the Backend

From the project root directory:

```bash
source venv/bin/activate
uvicorn main:app --reload
```

The backend API will be available at `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

### Start the Frontend

In a new terminal, from the `frontend` directory:

```bash
cd frontend
npm start
```

The React application will open automatically at `http://localhost:3000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/products` | Get all products |
| GET | `/product/{id}` | Get product by ID |
| POST | `/products` | Create a new product |
| PUT | `/products` | Update a product |
| DELETE | `/products` | Delete a product |

## Database Schema

### Product Table

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| name | String | Product name |
| description | String | Product description |
| price | Float | Product price |
| quantity | Integer | Available quantity |

## Usage

1. **Add a Product**: Fill in the form with product details and click "Add"
2. **Edit a Product**: Click the "Edit" button on any product row, modify the form, and click "Update"
3. **Delete a Product**: Click the "Delete" button and confirm the deletion
4. **Search Products**: Use the search bar to filter products by ID, name, or description
5. **Sort Products**: Click on column headers (ID, Name, Price, Quantity) to sort

## Development

### Initial Database Setup

The application automatically creates the database tables on startup and seeds initial product data if the database is empty.

### CORS Configuration

The backend is configured to accept requests from `http://localhost:3000`. Modify the CORS settings in [main.py](main.py#L12-L15) if needed.

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| DATABASE_URL | PostgreSQL connection string | `postgresql://user:pass@localhost:5432/db` |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built as part of learning FastAPI and React integration
- Inspired by modern product management systems
