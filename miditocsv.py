import sys
from py_midicsv.midicsv import parse

def main():
    if len(sys.argv) < 3:
        print("Not enough arguments passed in!")
    else:
        csv_data = parse(sys.argv[1])
        output_file = open(sys.argv[2], "w")
        for line in csv_data:
            output_file.write(line)
        output_file.close()

if __name__ == "__main__":
    main()