# faCRSA
## About
A fully automated pipeline for the high-throughput analysis of crop root system architecture.

## Installation and launcher
faCRSA has been tested under Ubuntu 18.04 LTS, CentOS 7, macOS 12 Monterey, and Windows 10 with Python 3.6.0. **Before installing faCRSA, you must install Anaconda.**
### Install with Conda (Recommended 😊)
##### 1. Install faCRSA from PyPI
```pyt
# Create a clear environment for faCRSA
conda -create -n facrsa python=3.6.0
conda activate facrsa

# Install faCRSA
pip install faCRSA
```
##### 2. Launch faCRSA
```pyt
# Launch task queue
facrsa-queue

# Launch faCRSA web
facrsa-web
```
### Install manually
##### 1. Clone faCRSA Github  repository
```pyt
# We recommend cloning the faCRSA repository into a clear folder.
cd {your folder}
git clone https://github.com/njauzrn/facrsa.git
cd facrsa/faCRSA
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

# Launch faCRSA web
flask run
```