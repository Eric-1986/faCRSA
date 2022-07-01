# faCRSA 
A fully automated pipeline for the high-throughput analysis of crop root system architecture. 
## Use faCRSA webserver
❤️ Try faCRSA at https://root.aiphenomics.com/. You can see help documents about faCRSA usage on the Github page (Section 3. Usage) and at https://root.aiphenomics.com/faq.
## Deploy faCRSA in a private environment
### 1. Installation and launcher
- faCRSA has been tested under Ubuntu 18.04 LTS, CentOS 7, macOS 12 Monterey, and Windows 10 with Python 3.6.0. 
- Install with Conda or manually.
- ⚠️**Before installing faCRSA, you must install Anaconda.**
#### 1.1 Install with Conda (Recommended 😊)
##### 1.1.1 Install faCRSA from PyPI
```pyt
# Create a clear environment for faCRSA
conda 
create -n facrsa python=3.6.0
conda activate facrsa

# Install faCRSA
pip install faCRSA
```
##### 1.1.2 Launch faCRSA
```pyt
# Launch task queue
facrsa-queue

# Create a new cmd window
# Launch faCRSA web
facrsa-web
```
##### 1.1.3 Open web page
Copy the URL address (e.g., http://127.0.0.1:5000/) output from the cmd window and open it in the browser.
#### 1.2 Install manually
##### 1.2.1 Clone faCRSA Github  repository
```pyt
# We recommend cloning the faCRSA repository into a clear folder.
cd {your folder}
git clone https://github.com/njauzrn/faCRSA.git
cd faCRSA
```
##### 1.2.2 Install Python requirements
```pyt
# Create a clear environment for faCRSA
conda create -n facrsa python=3.6.0
conda activate facrsa

# Install Python requirements
pip install -r requirements.txt
```
##### 1.2.3. Launch faCRSA
```pyt
# Launch task queue
python huey_consumer.py task_queue.huey

# Create a new cmd window
# Launch faCRSA web
flask run
```
##### 1.2.4. Open web page
Copy the URL address (e.g., http://127.0.0.1:5000/) output from the cmd window and open it in the browser.
### 2. faCRSA initialization
When you visit the web page for the first time, it will automatically jump to the initialization page. You can set  SMTP server information in this page, which used to notify task status. If you don't need this function, please click the following link to skip.
![[Pasted image 20220701121713.png]]
### 3. Usage
#### 3.1 Submit a Task
1. Click "Submit a new task" to load a task. **We recommend you create an account to manage tasks and upload private plugins.**
2. Input task information.
	- Task Name: set a name to distinguish different tasks.
	- Description: set some information about this task.
	- Pixel-to-cm Conversion Factor (CF): ![image](https://user-images.githubusercontent.com/71422762/176850182-3b7ecd01-64c1-4c15-bcce-21e26f749706.png)
	- Segmentation Plugin: select a model to segment root images (default: RootSeg). You can upload a private plugin to segment more types of crops and image backgrounds  <span id="jump">(Click here to study how to develop it).
	- 
