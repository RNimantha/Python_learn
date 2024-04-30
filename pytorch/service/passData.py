from service.network import Net
from service.train import TrainData
import torch
import torchvision as tv
from torchvision import transforms, datasets

class PassData():
    def __init__(self):
        self.train = TrainData()

    def data_pass(self):

        train = datasets.MNIST("", train=True, download=True,
                       transform= transforms.Compose([transforms.ToTensor()]))
        trainset = torch.utils.data.DataLoader(train , batch_size=10, shuffle=True)
        net = Net()
        TrainData().train_data(trainset, net)
        
        # return output