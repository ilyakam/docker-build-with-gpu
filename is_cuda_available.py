import torch

has_cuda = torch.cuda.is_available()

print(f'Has CUDA? {has_cuda}')
