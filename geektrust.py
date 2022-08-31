from sys import argv
from src.power import calculate_power

def main():
    
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """

    print(calculate_power(2, 1, "E", 4, 3))

    
if __name__ == "__main__":
    main()