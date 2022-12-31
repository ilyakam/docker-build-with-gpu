import torch

def init():
    print('Ran `init()` in `app.py`')

def inference(model_inputs:dict) -> dict:
    print(f'Ran `inference()` in `app.py` with a dict of {model_inputs}')

    has_cuda = torch.cuda.is_available()

    return {"has_cuda": has_cuda}
