# 🔗 Guide

- [faCRSA](#facrsa)
  * [Use faCRSA webserver](#use-facrsa-webserver)
  * [Deploy faCRSA in a private environment](#deploy-facrsa-in-a-private-environment)
    + [1. Installation and launcher](#1-installation-and-launcher)
      - [1.1 Install with Conda (Recommended)](#11-install-with-conda--recommended)
        * [1.1.1 Install faCRSA from PyPI](#111-install-facrsa-from-pypi)
        * [1.1.2 Launch faCRSA](#112-launch-facrsa)
        * [1.1.3 Open web page](#113-open-web-page)
      - [1.2 Install manually](#12-install-manually)
        * [1.2.1 Clone faCRSA Github  repository](#121-clone-facrsa-github--repository)
        * [1.2.2 Install Python requirements](#122-install-python-requirements)
        * [1.2.3. Launch faCRSA](#123-launch-facrsa)
        * [1.2.4. Open web page](#124-open-web-page)
    + [2. faCRSA initialization](#2-facrsa-initialization)
  * [Usage](#usage)
    + [1 Submit a Task](#1-submit-a-task)
    + [2 View results](#2-view-results)
    + [3 Upload private plugin](#3-upload-private-plugin)
    + [4 Use private plugin](#4-use-private-plugin)
  * [Development](#development)
    + [1. Private plugin](#1-private-plugin)
      - [Development guide](#development-guide)
    + [2 Training model](#2-training-model)
  * [Update](#update) (2022.08.22)
  * [TODO](#todo)
  * [Contact](#contact)

# faCRSA

An automated pipeline for high-throughput analysis of crop root system architecture. 
![pipeline](https://user-images.githubusercontent.com/71422762/183272665-4d23a7fd-d7f2-4851-abc0-53eabeec5f9e.png)

## Use faCRSA webserver

❤️ Try faCRSA at https://facrsa.aiphenomics.com/. You can see help documents about faCRSA usage on the Github page (Section 3. Usage).

## Deploy faCRSA in a private environment

### 1. Installation and launcher

- faCRSA has been tested under Ubuntu 18.04 LTS, CentOS 7, macOS 12 Monterey, and Windows 10 with Python 3.6.0. 
- Install with Conda or manually.
- ⚠️**Before installing faCRSA, you must install Anaconda.**

#### 1.1 Install with Conda (Recommended)

##### 1.1.1 Install faCRSA from PyPI

```pyt
# Create a clear environment for faCRSA
conda create -n facrsa python=3.6
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
conda activate facrsa
facrsa-web
```

##### 1.1.3 Open web page

Copy the URL address (e.g. http://127.0.0.1:5000/) output from the cmd window and open it in the browser.

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
conda create -n facrsa python=3.6
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
conda activate facrsa
flask run
```

##### 1.2.4. Open web page

Copy the URL address (e.g. http://127.0.0.1:5000/) output from the cmd window and open it in the browser.

### 2. faCRSA initialization

When you visit the web page for the first time, it will automatically jump to the initialization page. You can set  SMTP server information in this page, which used to notify task status. If you don't need this function, please click the following link to skip.

<img src="https://user-images.githubusercontent.com/71422762/176860754-d8852989-2000-4419-82f0-e0e7a17cfbec.png" alt="image" style="zoom:82%;" />

## Usage

### 1 Submit a Task

1. Click "Submit a new task" to load a task. **We recommend you create an account to manage tasks and upload private plugins.**
2. Input task information and upload images.
   - Task Name: set a name to distinguish different tasks.
   - Description: set some information about this task.
   - Pixel-to-cm Conversion Factor (CF): ![image](https://user-images.githubusercontent.com/71422762/176860806-139ebc3d-8daa-4f32-9655-1f831065af2a.png)
   - Segmentation Plugin: select a model to segment root images (default: RootSeg). You can upload a private plugin to segment more types of crops and imaging backgrounds (click here to study how to develop it).
   - E-mail (Optional): receive task notification emails.
   - Upload: 
     - Only several formats (`jpg / png / zip`) are allowed to upload.
     - A single task can only upload the same format.
3. Submit your task and it will automatically redirect to the schedule page.
4. You will be redirected to the result page and receive a task notification email.

### 2 View results

1.  When the task is completed, you will receive a notification email with a link to the result page.
2.  You can viste each results online or download them as a zipfile.

### 3 Upload private plugin

⚠️**Before uploading, you must create an account.**

1.  Click "Add a plugin" in the "My Plugin" page.
2.  Input plugin information and upload files.

### 4 Use private plugin

Select each plugin in the "add task" page.

## Development

### 1. Private plugin

🔗 Please click https://file.aiphenomics.com/demo_plugin.zip to download the demo code of private plugin.<br>⚠️Each plugin must be developed based on the following packages.

```pyt
numpy==1.19.2
tensorflow==2.4.0
```

The deep learning model must be constructed by Kears in Tensorflow (code: <code>from tensorflow.keras.layers import *</code>).

#### Development guide

1. Plugin structure:

- network.py: the deep learning model constructed in the Python programming language.

 > This file must include a function named "main" without any parameters. 

- weight.h5: model weight file (**must be .h5 format**)

2. Package these files in zip format.

- weight.h5: model weight file (**must be .h5 format**)

2. Package these files in zip format.
3. Test the availability of each plugin and upload it to faCRSA.

### 2 Training model

RootSeg could be trained for images from other crops and imaging backgrounds.

1. Download the model folder (<code>faCRSA/RootSeg</code>) and unzip the package.
2. Use the produce_train_txt script to generate a training file that includes image paths.
3. Open the train script and set customized parameters, such as learning rate, training epoch and date folder.
4. Switch to the training environment (e.g. facrsa) and start model training.

## Update

- 2022.08.22

  1. Merge a horizontally flipped image with the initial masked image to improve segment accuracy.

- 2022.08.21

  1. Add the model training scripts for users to easily train the model.

- 2022.08.06

  1. Support to measure root  angle (<code>Alpha</code> Version).

  - ![angle](https://user-images.githubusercontent.com/71422762/183234733-7ff22856-bd73-4813-a838-4210c5ae3e02.png) 

  2. Fix several bugs.

  3. Increase the speed of analysis.

## TODO

- [ ] Update weight files.

- [ ] Improve the measurement accuracy of root angle.

## Contact

If you have any questions or suggestions, please contact Ruinan Zhang (2020801253@stu.njau.edu.cn) at Nanjing Agricultural University.
