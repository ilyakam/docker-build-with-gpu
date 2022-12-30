import torch

def init():
    print('Ran `init()` in `app.py`')

def inference():
    print('Ran `inference()` in `app.py`')

    has_cuda = torch.cuda.is_available()

    return {"has_cuda": has_cuda}
