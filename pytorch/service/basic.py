import torch

class BasicTorch():
    def __init__(self):
        pass

    def basic(self):
        x = torch.rand(5, 3)
        print(x)

        y = torch.tensor([3,2])
        print(y)