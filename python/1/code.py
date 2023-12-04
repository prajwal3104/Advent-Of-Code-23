def process_string(input_string):
    numbers = [char for char in input_string if char.isdigit()]

    if len(numbers) >= 2:
        first_number = numbers[0]
        last_number = numbers[-1]
        result = int(first_number + last_number)
    elif len(numbers) == 1:
        result = int(numbers[0] * 2)
    else:
        result = 0

    return result

def main():
    total_sum = 0

    input_file_path = "/Users/prajwal/Developer/Advent-Of-Code-23/python/1/input.txt"

    with open(input_file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            output = process_string(line)
            total_sum += output

        print(f"Final result: {total_sum}")

if __name__ == "__main__":
    main()
