<p align="center"><img alt="image" src="pictures/image.png" /></p>

# Data Analytics Dashboard

## Overview

The Data Analytics Dashboard is an interactive web application built with Dash, allowing users to upload their datasets and perform various types of data analysis. The application supports CSV and Excel file formats and provides tools for data visualization and statistical summary.

## Features

- **File Upload**: Easily upload your CSV or Excel files.
- **Interactive Table**: View your data in a user-friendly table.
- **Data Visualization**: Generate scatter plots to visualize the relationships between variables.
- **Responsive Design**: Access the dashboard from any device with a modern web browser.

## Project Structure

```
data_analytics_dashboard/
│
├── app/
│ ├── init.py
│ ├── layout.py
│ ├── callbacks.py
│ └── assets/
│ ├── styles.css
├── config.py
├── run.py
└── requirements.txt
```

- `app/`: Directory containing the code for the web application.
  - `__init__.py`: Initialization of the Dash app.
  - `layout.py`: Layout definition for the app page.
  - `callbacks.py`: Callbacks for interactivity.
  - `assets/`: Folder for static files (e.g., CSS styles).
- `config.py`: Application configuration file.
- `run.py`: File to run the web application.
- `requirements.txt`: Project dependencies file.

## Running the Application

### Prerequisites

- Python 3.6 or higher

### Setup

1. **Clone the repository**:

```sh
git clone https://github.com/Bebrowskiy/data_analytics_dashboard.git
cd data_analytics_dashboard
```

2. **Create and activate a virtual environment**:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install dependencies**:

```sh
pip install -r requirements.txt
```

4. **Run the web application**:

```sh
python run.py
```

Then, open a web browser and go to `http://127.0.0.1:8050/` to start using the application.

## Usage

1. **Upload a Dataset**:

   - Click on the "Select Files" button or drag and drop your CSV or Excel file into the designated area.

2. **View and Analyze Data**:
   - After uploading, your data will be displayed in an interactive table.
   - A scatter plot will be automatically generated using the first two columns of your dataset.
