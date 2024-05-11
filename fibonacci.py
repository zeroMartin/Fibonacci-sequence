def fibonacci():
    a = 10
    sequence = [1, 1]
    for i in range(a):
        seq = sequence[-1] + sequence[-2]
        sequence.append(seq)
    return sequence

print(fibonacci())
