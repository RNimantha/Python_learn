# Import the BasicTorch class
from service.basic import BasicTorch
from service.network import Net
from service.passData import PassData

# Define the main function
def main():
    data = PassData()
    output = data.data_pass()
    print(output)

if __name__ == "__main__":
    main()
