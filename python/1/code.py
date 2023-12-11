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

    input_file_path = "your_input_file.txt"

    try:
        with open(input_file_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            output = (line)
            total_sum += output

        print(f"Final result: {total_sum}")

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")

if __name__ == "__main__":
    main()
