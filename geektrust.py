from sys import argv
from src.custom_exceptions import *
from src.gman import Gman
from src.coordinate import Coordinate

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()

    if (len(Lines) != 3):
        raise InvalidInputFile()

    for i in range(len(Lines)):
        if (i == 0):
            src_lst = Lines[i].strip().split(" ")

            if (len(src_lst) != 4):
                raise InvalidSource()
            elif (src_lst[0] != "SOURCE"):
                raise SourceNotPresent()
            elif (src_lst[3] not in ["N", "S", "W", "E"]):
                raise InvalidDirection()

            source = Coordinate(src_lst[1], src_lst[2])
            direction = src_lst[3]

        elif (i == 1):
            dest_lst = Lines[i].strip().split(" ")

            if (len(dest_lst) != 3):
                raise InvalidDestination()
            elif (dest_lst[0] != "DESTINATION"):
                raise DestinationNotPresent()

            destination = Coordinate(dest_lst[1], dest_lst[2])

        else:
            if Lines[i] == "PRINT_POWER":
                gman = Gman(source, direction, destination)
                #power = calculate_power(int(src_lst[1]), int(src_lst[2]), src_lst[3], int(dest_lst[1]), int(dest_lst[2]));
                print("POWER " + str(gman.calculate_remaining_power()))
            else:
                raise PrintCommandNotPresent()
    
if __name__ == "__main__":
    main()