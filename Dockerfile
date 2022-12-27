# Must use a Cuda version 11+
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

# Set up a working directory and copy everything over
WORKDIR /
ADD . .

RUN pip install -r requirements.txt

RUN python is_cuda_available.py
