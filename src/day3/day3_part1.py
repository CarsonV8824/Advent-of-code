def staircase(filename):
    with open(filename, "r") as file:
        file_lines = file.readlines()
        
    file_lines = [line.replace("\n","") for line in file_lines]
    file_lines = [int(line) for line in file_lines]
    
    for big_num in file_lines:
        first_num = 0
        first_num_index = 0
        
        for index, num in enumerate(big_num):
            if num > first_num:
                first_num = num
                first_num_index = index
        
        if first_num_index == (len(str(big_num)) - 1):
            for i in range(0, len(str(big_num)) - 2):
                pass
    
if __name__ == "__main__":
    print(staircase("src/day3/test_day3.txt"))