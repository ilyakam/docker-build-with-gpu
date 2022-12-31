# Must use a Cuda version 11+
FROM ilyakam/tts_w_deps:001

# Set up a working directory and copy everything over
WORKDIR /
ADD . .

RUN pip install -r requirements.txt

RUN python is_cuda_available.py

EXPOSE 8000

CMD python -u server.py
