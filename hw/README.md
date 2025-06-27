# llmz
just some dang ol research, man

## hw1: Elasticsearch 8.17.6 Setup with Jupyter Notebook

### Setup Instructions

#### 1. Python Environment Setup (Official Python.org Method)

Create and activate a virtual environment:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

Install required packages:
```bash
# Upgrade pip to latest version (recommended)
python3 -m pip install --upgrade pip setuptools wheel

# Install all dependencies
python3 -m pip install -r requirements.txt
```

#### 2. Start Elasticsearch

```bash
docker-compose up -d
```

Wait for Elasticsearch to be healthy:
```bash
# Check if Elasticsearch is running
curl localhost:9200
```

#### 3. Launch Jupyter Notebook

```bash
jupyter notebook
```

This will open Jupyter in your browser. Create a new notebook to start working with data.

### Example Workflow

Your notebook can:
1. Use `requests` to download data from APIs
2. Process data with `numpy` and `pandas`
3. Insert processed data into Elasticsearch
4. Visualize results with `matplotlib`

### Stopping Services

```bash
# Stop Elasticsearch
docker-compose down

# Deactivate virtual environment
deactivate
```
