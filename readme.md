# faCRSA
## About
A fully automated pipeline for the high-throughput analysis of crop root system architecture.

## Installation and launcher
- faCRSA has been tested under Ubuntu 18.04 LTS, CentOS 7, macOS 12 Monterey, and Windows 10 with Python 3.6.0. 
- ⚠️**Before installing faCRSA, you must install Anaconda.**
### Install with Conda (Recommended 😊)
##### 1. Install faCRSA from PyPI
```pyt
# Create a clear environment for faCRSA
conda 
create -n facrsa python=3.6.0
conda activate facrsa

# Install faCRSA
pip install faCRSA
```
##### 2. Launch faCRSA
```pyt
# Launch task queue
facrsa-queue

# Create a new cmd window
# Launch faCRSA web
facrsa-web
```
##### 3. Open web page
Copy the URL address (http://127.0.0.1:5000/) output from the cmd window and open it in the browser.
### Install manually
##### 1. Clone faCRSA Github  repository
```pyt
# We recommend cloning the faCRSA repository into a clear folder.
cd {your folder}
git clone https://github.com/njauzrn/faCRSA.git
cd faCRSA
```
##### 2. Install Python requirements
```pyt
# Create a clear environment for faCRSA
conda create -n facrsa python=3.6.0
conda activate facrsa

# Install Python requirements
pip install -r requirements.txt
```
##### 3. Launch faCRSA
```pyt
# Launch task queue
python huey_consumer.py task_queue.huey

# Create a new cmd window
# Launch faCRSA web
flask run
```
##### 4. Open web page
Copy the URL address (http://127.0.0.1:5000/) output from the cmd window and open it in the browser.
## faCRSA initialization
⚠️
