# E-Commerce Data Aggregation Pipeline

This project demonstrates how to analyze e-commerce customer purchase data and generate insights about high-value customers using an aggregation pipeline in MongoDB. It uses **Python**, **Beanie (MongoDB ODM)**, and **MongoDB Atlas** to store and process data.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Prerequisites

Before you can run this project locally, make sure you have the following installed:

- **Python 3.8+**: If you don't have it, download and install from [python.org](https://www.python.org/downloads/).
- **MongoDB Atlas Account**: You need a MongoDB Atlas cluster. Sign up [here](https://www.mongodb.com/cloud/atlas) and create a new cluster.
- **MongoDB URI**: A connection string to your MongoDB Atlas database (e.g., `mongodb+srv://<username>:<password>@<cluster-url>/<database-name>`).

---

## Installation

Follow these steps to get your local environment set up:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/ecommerce-pipeline.git
   cd ecommerce-pipeline
