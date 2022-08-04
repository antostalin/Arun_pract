
if __name__ == '__main__':
    fibs = [0, 1]
    num = int(input('How many  fibnocci series number you want?'))
    for i in range(num-2):
        fibs.append(fibs[-2] + fibs[-1])

    print(fibs)