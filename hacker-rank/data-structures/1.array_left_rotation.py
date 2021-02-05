def rotate(items):
    return items[1:] + [items[0]]

# [Input 1] n: number of items in array, d: number of left rotations to do
n, d = map(int, raw_input().split(' '))

# [Input 2] items: list of integers
items = map(int, raw_input().split(' '))

# [Process] Rotate list
for i in range(d):
    items = rotate(items)

# [Output] Rotated list
print ' '.join(map(str, items))

