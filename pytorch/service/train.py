import torch
import torch.optim as optim
import torch.nn.functional as f




class TrainData():
    def __init__(self):
        
        self.EPOCHS = 3
        

    def train_data(self, trainset, net):
        optimizer = optim.Adam(net.parameters(), lr=0.001)

        for epoch in range(self.EPOCHS):
            for data in trainset:
                X,y = data
                net.zero_grad()
                output = net(X.view(-1, 28*28))
                loss = f.nll_loss(output, y)
                loss.backward()
                optimizer.step()
            print(loss)

        # check accuracy
        correct = 0
        total = 0 
        
        with torch.no_grad():
            for data in trainset:
                X,y = data
                output = net(X.view(-1, 784))
                for idx , i in enumerate(output):
                    if torch.argmax(i) == y[idx]:
                        correct += 1
                    total += 1
        print("Accuracy: ", round(correct/total, 3))





