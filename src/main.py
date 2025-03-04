import sys

def run_querys(input_matrix, querys):
    debug = ""
    result = ""
    column_count = len(input_matrix[0])
    row_count = len(input_matrix)
    diagonal_slope = len(input_matrix[0]) / len(input_matrix)

    debug += f"Matrix diagonal slope {diagonal_slope}\n"

    for query in querys:
        query_list = query.split(" ")
        from_row = int(query_list[0]) - 1
        from_col = int(query_list[1]) - 1
        to_row = int(query_list[2]) - 1
        to_col = int(query_list[3]) - 1

    
        debug += f"\nFrom Row: {input_matrix[from_row]}, To Row: {input_matrix[to_row]}, Query: {from_row}, {from_col} to {to_row},{to_col}\n"
    
        diagonal_slope = column_count / row_count

        try:
            from_value = int(input_matrix[from_row][from_col])
            to_value = int(input_matrix[to_row][to_col])
        except IndexError:
            debug += "neither, out of bounds\n"
            continue
   
        # Check that query doesn't move diagonal
        try:
            slope = abs(to_col - from_col) / abs(to_row - from_row)
            debug += f"Slope: {slope}, from {from_col}, {from_row} to {to_col}, {to_row}, from value {from_value}, to value {to_value}\n"
            if abs(slope) == diagonal_slope:
                debug += "neither, diagonal\n"
                result += "neither\n"
                continue
        except ZeroDivisionError:
            debug += "Not a diagonal\n"
            pass


        if s := from_value == to_value and from_value == 1:
            result += "decimal\n"
        elif s := from_value == to_value and from_value == 0:
            result += "binary\n"
        else:
            result += "neither\n"

    print(debug)

    return result


def load_input():
    result = ""
    input_matrix = []
    querys = []

    import sys
    import readline

    header_line = sys.stdin.readline().strip()
    header = header_line.split()
    input_rows = int(header[0])

    # print(input_rows)

    if input_rows > 1000:
        print(f"To many input lines {i}")
        exit(1)

    for i in range(input_rows):

        line = sys.stdin.readline().strip()

        if len(line) > 1000:
            print(f"To big input line {len(line)}")
            exit(1)

        input_matrix.extend(line.split())

    querys_count = int(sys.stdin.readline().strip())

    for i in range(querys_count):
        querys.append(sys.stdin.readline().strip())

    # print(input_matrix)
    # print(querys)

    return input_matrix, querys


def main():
    input_data, querys = load_input()
    result = run_querys(input_data, querys)
    print(result)

if __name__ == "__main__":
    main()


