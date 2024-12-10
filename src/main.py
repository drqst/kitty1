import sys

# things = [];

global things
things = [1111100000], [1111000000], [1110000011], [0x111100111], [0x011111111]

def find_friends(howMany):
    r = things[howMany]
    return r

def main():
    args = sys.argv[1:]

    if len(args) >= 0:
        howMany =  int(args[0])
        result = find_friends(howMany)
        print(f"Result is {result}")
    else:
        print ("Specity just one variable, if none, how many?")


if __name__ == "__main__":
    main()
