# abcdesktop-python-gpu-numpy-sample
abcdesktop python gpu numpy sample sort 

## Add the application to your abcdesktop instance 

<img width="1440" alt="Screenshot 2025-03-21 at 13 24 43" src="https://github.com/user-attachments/assets/a6e0821e-bff7-4d3b-a89d-41abb40deb8c" />


## Run nvidismi

On your host run `nvidia-smi` command line

```
nvidia-smi 
```

python3 is running 

```
Fri Mar 21 13:42:40 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.144.03             Driver Version: 550.144.03     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  Quadro M620                    Off |   00000000:01:00.0  On |                  N/A |
| N/A   54C    P0             N/A /  200W |    1568MiB /   2048MiB |    100%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A     96467      C   python3                                      1562MiB |
+-----------------------------------------------------------------------------------------+
```
