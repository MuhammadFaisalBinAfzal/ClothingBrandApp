<div align="center">
  <h1>👕 Clothing Brand Manager - Ultimate POS & Inventory 📈</h1>
  <p>A modern, robust Point of Sale and Inventory Management desktop application built with Python and CustomTkinter.</p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white" alt="SQL Server">
  <img src="https://img.shields.io/badge/CustomTkinter-000000?style=for-the-badge&logo=python&logoColor=white" alt="CustomTkinter">
</p>

---

## 🚀 Overview
**Clothing Brand Manager** is designed to streamline the operations of a retail clothing business. It moves away from cumbersome spreadsheets to a sleek, dark-themed UI that manages inventory, processes sales, tracks daily expenses, and generates insightful financial reports with automated charting.

## 🌟 Key Features
- **📦 Inventory Management:** Easily add, categorize, and update product stocks.
- **🛒 Point of Sale (POS):** Fast checkout system with real-time stock deductions.
- **💸 Expense Tracking:** Keep track of business expenses to calculate true net profit.
- **📊 Business Analytics:** Automatically generate and export financial reports (CSV, PNG, PDF) using Matplotlib.
- **🛡️ Secure Database:** Robust backend powered by Microsoft SQL Server. Environment-based connection scaling.

---

## 📸 Screenshots
Here is a look at the application in action:

<img width="1919" height="1011" alt="Screenshot 2026-08-12 113753" src="https://github.com/user-attachments/assets/0efc3307-f217-4ab5-8bdd-66930efb87b6" />

<img width="1919" height="1005" alt="Screenshot 2026-08-12 113802" src="https://github.com/user-attachments/assets/fc7db203-4914-4c3e-a574-a10a6d255449" />

<img width="1908" height="1007" alt="Screenshot 2026-08-12 113811" src="https://github.com/user-attachments/assets/c07e780c-ee9b-4c9b-9b85-35f9324a2a6f" />

<img width="1919" height="1011" alt="Screenshot 2026-08-12 113827" src="https://github.com/user-attachments/assets/e5194385-6d60-41d3-88b8-60e82ab0951c" />

<img width="1919" height="1011" alt="Screenshot 2026-08-12 113838" src="https://github.com/user-attachments/assets/a83d4ab7-fd89-4803-b0d7-a17c12383852" />

---

## ⚙️ Tech Stack
- **Frontend / GUI**: `CustomTkinter` (Modern styling on top of Tkinter)
- **Backend / Logic**: Python 3.8+
- **Database**: Microsoft SQL Server (via `pyodbc`)
- **Data Viz & Export**: `matplotlib`, `cairosvg`, `Pillow`
- **Environment Management**: `python-dotenv`

---

## 🛠️ Installation & Setup

### 1. Prerequisites
- **Python 3.8+** installed on your system.
- **Microsoft SQL Server** (e.g., SQLEXPRESS) and **ODBC Driver 17 for SQL Server** installed.

### 2. Database Initialization
1. Open SQL Server Management Studio (SSMS).
2. Create a new database named `BrandManagerDB`.
3. Open the `SQL queries/SQLQuery1.sql` file provided in this repository and execute it to create the required tables.

### 3. Application Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MuhammadFaisalBinAfzal/ClothingBrandApp.git
   cd ClothingBrandApp
   ```

2. **Set up environment variables:**
   - Rename `example.env` to `.env`
   - Update the `.env` file with your SQL Server instance name.
   ```env
   SQL_SERVER_NAME=YOUR-PC-NAME\SQLEXPRESS
   SQL_DATABASE_NAME=BrandManagerDB
   ```

3. **Create a Virtual Environment (Recommended):**
   This keeps dependencies isolated and looks highly professional.
   ```bash
   python -m venv venv
   
   # Activate it on Windows:
   venv\Scripts\activate
   
   # Activate it on macOS/Linux:
   source venv/bin/activate
   ```

4. **Install dependencies:**
   Make sure your virtual environment is activated before running this!
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python main.py
   ```

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).