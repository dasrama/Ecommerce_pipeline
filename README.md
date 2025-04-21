# E-Commerce Data Aggregation Pipeline

This project demonstrates how to analyze e-commerce customer purchase data and generate insights about high-value customers using an aggregation pipeline in MongoDB. It uses **Python**, **Beanie (MongoDB ODM)**, and **MongoDB Atlas** to store and process data.

---

## Prerequisites

Before you can run this project locally, make sure you have the following installed:

- **Python 3.8+**: If you don't have it, download and install from [python.org](https://www.python.org/downloads/).
- **MongoDB Atlas Account**: You need a MongoDB Atlas cluster. Sign up [here](https://www.mongodb.com/cloud/atlas) and create a new cluster.
- **MongoDB URI**: A connection string to your MongoDB Atlas database (e.g., `mongodb+srv://<username>:<password>@<cluster-url>/<database-name>`).

---

## Installation

1. Clone the repository:
   ```bash
   https://github.com/dasrama/Ecommerce_pipeline.git
   cd Ecommerce_pipeline
   ```

2. Set up a virtual environment and install dependencies:

   - **On Windows**:
     ```bash
     py -3 -m venv venv
     venv\Scripts\activate
     pip install -r requirements.txt
     ```

   - **On macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```

3. Configure environment variables:
   - Create a `.env` file in the project root.
   - Add the following variables:
     ```env
     DATABASE_URL=mongo_url_from_cloud
     ```

4. Start the FastAPI server:
   ```bash
   uvicorn backend.main:app --reload
   ```

5. Access the API documentation:
   Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

