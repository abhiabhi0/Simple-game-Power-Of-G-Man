from sys import argv
from src.power import calculate_power

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()

    for i in range(len(Lines)):
        if (i == 0):
            src_lst = Lines[i].strip().split(" ")
        elif (i == 1):
            dest_lst = Lines[i].strip().split(" ")
        else:
            if Lines[i] == "PRINT_POWER":
                power = calculate_power(int(src_lst[1]), int(src_lst[2]), src_lst[3], int(dest_lst[1]), int(dest_lst[2]));
                print("POWER " + str(power))
    
if __name__ == "__main__":
    main()