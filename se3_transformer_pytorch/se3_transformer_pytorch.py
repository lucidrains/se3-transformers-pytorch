import torch
import torch.nn.functional as F
from torch import nn, einsum
from einops import rearrange, repeat

class SE3Transformer(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x
