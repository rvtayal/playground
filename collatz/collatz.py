def get_collatz_path(num):
    path = [num]
    cur = num
    while cur != 1:
        if cur % 2 == 0:
            cur /= 2
        else:
            cur = 3*cur + 1
        path += [int(cur)]
    return path


if __name__ == "__main__":
    print(get_collatz_path(4))
    print(get_collatz_path(1))
    print(get_collatz_path(15))