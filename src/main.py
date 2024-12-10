import sys

def load_input(filename):
    input_map = []
    header = []
    querys = []

    with open(filename, "r") as f:
        line = f.readline().strip()
        header = line.split(" ")
        rows = int(header[0])
        for i in range(rows):
            if i > 1000:
                print("To many input lines")
                exit(1)

            line = f.readline().strip()
            if len(line) > 1000:
                print("To big input line")
                exit(1)

            input_map.append(line)


        number_of_querys = int(f.readline().strip())

        for i in range(number_of_querys):
            querys.append(f.readline().strip())

    complete_array = [header, list(input_map), querys]

    return complete_array

def run_querys(input_matrix, querys):
    result = ""
    for query in querys:
        query_list = query.split(" ")
        from_row = int(query_list[0]) - 1 # zero indexed.
        from_col = int(query_list[1]) - 1 # zero indexed.
        to_row = int(query_list[2]) - 1 # zero indexed.
        to_col = int(query_list[3]) - 1 # zero indexed.

        # Check that query doesn't move diagonal

        # print(f"From Row: {input_matrix[from_row]}")
        # print(f"To Row:   {input_matrix[to_row]}")
        # print(f"From {from_row + 1, from_col + 1} / To {to_row + 1, to_col + 1}")

        try:
            slope = ((to_col + 1) - (from_col + 1)) / ((to_row + 1) - (from_row + 1))
            # print(f"Slope: {slope}")
            if abs(slope) == 1:
                result += "neither"
                continue
        except ZeroDivisionError:
            # Not a diagonal
            pass

            

        try:
            from_value = int(input_matrix[from_row][from_col])
            to_value = int(input_matrix[to_row][to_col])
        except IndexError:
            result += "neither, out of bounds\n"
            continue

        # print(f"From {from_row, from_col} / To {to_row, to_col} / Vals {from_value, to_value}")

        if s := from_value == to_value and from_value == 1:
            result += "decimal\n"
        elif s := from_value == to_value and from_value == 0:
            result += "binary\n"
        else:
            result += "neither\n"

    return result

def main():
    args = sys.argv[1:]

    if len(args) >= 0:
        filename =  args[0]
        input_matrix = load_input(filename)
        q = run_querys(input_matrix[1], input_matrix[2])
        # print(f"Input: {input_matrix[1]}")
        print(f"{q}")
    else:
        print ("No arguments")


if __name__ == "__main__":
    main()
