with open('dataset_24465_4.txt', 'r') as file_read, open('result.txt', 'w') as result:
    result.write('\n'.join(reversed(file_read.read().splitlines())))
