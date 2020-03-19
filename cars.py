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

