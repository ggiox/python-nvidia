# main.py
import torch

print(torch.cuda.is_available())
# Expected output: True
print(torch.cuda.device_count())
# Expected output: 1 (or more, depending on your system)
print(torch.cuda.current_device())
# Expected output: 0 (or the index of the current device)
print(torch.cuda.get_device_name(0))
# Expected output: Name of your GPU, e.g., 'NVIDIA GeForce RTX 1060'
print(torch.__version__)
# Expected output: Version of PyTorch, e.g., '1.7.1'

