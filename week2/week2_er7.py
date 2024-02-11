import sys

arg_len = len(sys.argv)
total = 0

for i in range(1, arg_len):
    total = total + int(sys.argv[i])

print(f'Average : {total/(arg_len-1)}')

