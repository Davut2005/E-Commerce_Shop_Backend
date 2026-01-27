#  E-Commerce Online Shop 

### The idea of the project

Backend E-Commerce Online Shop is an app connected to PostgreSQL local database with SQL queries where the users can order different categories of products,see the reviews, and the ratings of every product and even see the history of orders and its order items they made. 
The project also has the Payment and Checkout Page implementations

### Tech Stack

Python, FastAPI, PostgreSQL, psycopg2, uvicorn, uv

### Build the backend server in the terminal

1. Install all dependencies
uv sync

2. Run the servera
uv run uvicorn main:app --reload