import matplotlib.pyplot as plt
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.models as models
import torchvision.transforms as transforms
import torch.nn.functional as F


data_base = "/Users/ahmed/Desktop/Cars/"


#Set Up train Baloney
transform_train = transforms.Compose([ transforms.Resize(256),transforms.RandomCrop(256), transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
dataset_train =  torchvision.datasets.ImageFolder(root= data_base + "train" , transform = transform_train)
dataset_train_loader = torch.utils.data.DataLoader(dataset_train, batch_size = 8, shuffle = True)

#Set Up Test Baloney
transform_test = transforms.Compose([transforms.Resize(256), transforms.RandomCrop(256), transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
dataset_test = torchvision.datasets.ImageFolder(root = data_base + "test", transform = transform_test)
dataset_test_loader = torch.utils.data.DataLoader(dataset_test, batch_size = 8, shuffle = True)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(196608, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 10)
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        
        return F.log_softmax(x, dim=1)
        
net = Net()


criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

import torch.optim as optim

optimizer = optim.Adam(net.parameters(), lr = 0.001)

EPOCHS = 3

for epcoch in range(EPOCHS):
    for data in dataset_train:
        X, y = data
        net.zero_grad()
        output = net(X.view(-1,28*28))
        loss = F.nll_loss(output, y)
        loss.backward()
        optimizer.step()
    print(loss)
        