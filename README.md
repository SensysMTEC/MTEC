# M-TEC -  Dynamic DAG Application Scheduling for Multi-Tier Edge Computing

The framework of MTEC can be divided into two parts: **Orchestrator** and **Client**. Orchestrator is where all the orchestration started. When the orchestrator receives an application request (in DAG form), it starts orchestrating the task allocation based on the pre-profiled data of each client that joins the edge computing network, and then initiates the start of the application. On the clients' sides, each client is aware of the task allocation of the application and they perform the jobs assigned to them by the orchestrator individually and pass the intermediate results to the next task in the DAGs. The communication between clients is in a P2P manner. In the network, each node can act as an orchestrator as well as a client.

## Getting Started 

```
$sudo apt-get update
```

## Installation


The result presented in the paper are the average of more than 10 rounds of the experiments, so that we can eliminate the variation of the results due to the uncontrolled behavior of network and hardware.

We used python 3.7.2 on both clients' and orchestrator's side. To install python 3.7.2, do the following steps

First, install the required packages needed for building python
```
$sudo apt-get install build-essential checkinstall
$sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev liblzma-dev libopenblas-dev
```
Then, download python 3.7.2 and install it.
```
$sudo wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
$tar xzvf Python-3.7.2.tgz
$sudo ./configure
$sudo make altinstall
```
Once it is successfully installed, then install the required packages 
```BASH
$python3.7 -m pip install --upgrade pip
$python3.7 -m pip install -r requirements.txt
```
Notice that in one of the sample testing applications (video analytics), MXNET is needed. To install MXNET on arm based architecture, you can download the prebuild whl from [mxnet(arm64)](https://drive.google.com/file/d/1jr-kP1_zlLa9tx-GtdlBV3Nn20qRJgzY/view), then install it with 
```
python3.7 -m pip install mxnet_xxx.whl
```
Now, we have set up the client side, download governer.py and the edge_list.json(the IP addresses contained in this file should be adjusted to the devices in the network, the last device should always refer to the orchestrator), then starts governer.py and the client should start listening to the request from the orchestrator.

On the orchestrator side, I used conda to manage packages. The list of requirements can be found in orchestrator_requirements.txt. You can recreate the environment by doing 

```
$conda create -n <your_env> --file orchestrator_requirements.txt
```
The orchestrator takes in 6 arguments
- --app (e.g. lightgbm. Four applications are support, lightgbm, mapreduce, video_app and matrix, user can provide their own DAG form application by following the app_config.json in the profile_data section)
- --mc (e.g. Ed_mc_vid.xlsx. This file store the profile data of the devices in the network)
- --pf (Probability of failure threshold, Default to 0.25)
- --rd (Maximum replication degree, Default to 3)
- --jp (Joint optimization parameter alpha, Default to 0.5)
- --bt (Joint optimization parameter beta, Default to 0.5)
- --sch (Orchestration scheme, default to **mtec** )

An sample execution command is 
```
python mtec.py --app mapreduce --mc ED_mc_map.xlsx --sch mtec
```

## Acknowledgements

[MXNET(arm64)](https://drive.google.com/file/d/1jr-kP1_zlLa9tx-GtdlBV3Nn20qRJgzY/view)


