import sys

def load_input():
    input_map = []
    querys = []

    headers_for_data = sys.stdin.readline()

    numbers_of_data_rows = hedaers_for_data[0]
    numbers_of_data_columns = hedaers_for_data[1]

    # if j > 1000:
    #     print("To many input colums")
    #     exit(1)

    # if len(data_line[]) > 1000:
    #     print("To big input line")
    #     exit(1)

    for (i in range(0, number_of_data_lines)):
        input_map.append(sys.stdin.readline(data_line))

    headers_for_querys = sys.stdin.readline()
    number_of_querys = headers_for_querys[0]

    for i in range(number_of_querys):
        querys.append(f.readline().strip())

    complete_array = [input_map, querys]

    return complete_array

def run_querys(input_matrix, querys):
    result = ""
    column_count = len(input_matrix[0])
    row_count = len(input_matrix)

    result += f"Input Matrix: {input_matrix}\n"
    # result += f"Column count of matrix {column_count}\n"
    # result += f"Row count of matrix {row_count}\n"


    for query in querys:
        query_list = query.split(" ")
        from_row = int(query_list[0]) - 1
        from_col = int(query_list[1]) - 1
        to_row = int(query_list[2]) - 1
        to_col = int(query_list[3]) - 1

    
        result += f"From Row: {input_matrix[from_row]}, Query: {query_list[0]} {query_list[1]} {query_list[2]} {query_list[3]}\n"
        result += f"To Row:   {input_matrix[to_row]}\n"
    
        result += f"column count {column_count}, row count {row_count}\n"

        diagonal_slope = column_count / row_count

        result += f"diagonal slope {diagonal_slope}\n"
    
        # Check that query doesn't move diagonal
        try:
            slope = abs( ((to_col ) - (from_col)) / ((to_row) - (from_row)) )
            result += f"Slope: {slope}, to col {to_col}, from col {from_col}, to row {to_row} from row {from_row}\n"
            if abs(slope) == diagonal_slope:
                result += "neither\n"
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

        result += f"Divided by {from_row, from_col} / To {to_row, to_col} / Vals {from_value, to_value}\n"

        if s := from_value == to_value and from_value == 1:
            result += "decimal\n"
        elif s := from_value == to_value and from_value == 0:
            result += "binary\n"
        else:
            result += "neither\n"

    return result
f

def load_input():
    result = ""
    input_map = []
    querys = []

    import sys

    for line in sys.stdin:
        header = line.split(" ")
        rows = int(header[0])
        for i in range(rows):
            if i > 1000:
                result = "To many input lines"
                exit(1)

            line = f.readline().strip()
            if len(line) > 1000:
                result = "To big input line"
                exit(1)

            input_map.append(line)

    return result


def main():
    complete_array = load_input()
    result = run_querys(complete_array)
    print(result)ertdghsdf

if __name__ == "__main__":
    main()


