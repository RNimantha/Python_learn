# Import the BasicTorch class
from service.basic import BasicTorch
from service.network import Net
from service.passData import PassData
from service.convosional import Convo

REBUILD_DATA = True

# Define the main function
def main():
    # data = PassData()
    # data.data_pass()

    if REBUILD_DATA:
        dogsvcats = Convo()
        dogsvcats.convo()
    
if __name__ == "__main__":
    main()
