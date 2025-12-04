def staircase(filename):
    with open(filename, "r") as file:
        file_lines = file.readlines()
        
    file_lines = [line.replace("\n","") for line in file_lines]
    
if __name__ == "__main__":
    print(staircase("src/day3/test_day3.txt"))