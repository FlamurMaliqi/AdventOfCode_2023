# https://adventofcode.com/2023/day/9

FILE = 'input.txt'

# 1. part - What is the sum of these extrapolated values?
with open(FILE) as f:
    sum_of_extrapolated_values = 0

    # read the input line by line
    for line in f.readlines(): 
        sequence = list(map(int, line.split()))
        sequences = [sequence]

        # calculate diff sequences
        while not all(v == 0 for v in sequence):
            diff_sequence = [(sequence[i + 1] - sequence[i]) for i in range(len(sequence) - 1)]
            sequences.append(diff_sequence)
            sequence = diff_sequence

        # extrapolate next value in last sequence (sequence of all zeroes)
        sequences[-1].append(0)

        # extrapolate next value for the other sequences in reverse order
        for i in reversed(range(len(sequences) - 1)):
            sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])

        # add extrapolated value from the original sequence
        sum_of_extrapolated_values += sequences[0][-1]

    print(sum_of_extrapolated_values)


# 2. part - What is the sum of these extrapolated (backwards) values?
with open(FILE) as f:
    sum_of_extrapolated_values = 0

    # read the input line by line
    for line in f.readlines(): 
        sequence = list(map(int, line.split()))
        sequences = [sequence]

        # calculate diff sequences
        while not all(v == 0 for v in sequence):
            diff_sequence = [(sequence[i + 1] - sequence[i]) for i in range(len(sequence) - 1)]
            sequences.append(diff_sequence)
            sequence = diff_sequence

        # extrapolate previous value in last sequence (sequence of all zeroes)
        sequences[-1].insert(0, 0) 

        # extrapolate previous value for the other sequences in reverse order
        for i in reversed(range(len(sequences) - 1)):
            sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])

        # add extrapolated value to the original sequence
        sum_of_extrapolated_values += sequences[0][0]

    print(sum_of_extrapolated_values)

# 1. and 2. part combined
with open(FILE) as f:
    sum_of_extrapolated_values = 0
    sum_of_extrapolated_values_backwards = 0

    # read the input line by line
    for line in f.readlines(): 
        sequence = list(map(int, line.split()))
        sequences = [sequence]

        # calculate diff sequences
        while not all(v == 0 for v in sequence):
            diff_sequence = [(sequence[i + 1] - sequence[i]) for i in range(len(sequence) - 1)]
            sequences.append(diff_sequence)
            sequence = diff_sequence

        # extrapolate previous/next value in last sequence (sequence of all zeroes)
        sequences[-1].insert(0, 0)
        sequences[-1].append(0)

        # extrapolate previous/next value for the other sequences in reverse order
        for i in reversed(range(len(sequences) - 1)):
            sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])
            sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])

        # add extrapolated values to the original sequence
        sum_of_extrapolated_values_backwards += sequences[0][0]
        sum_of_extrapolated_values += sequences[0][-1]

    print(sum_of_extrapolated_values)
    print(sum_of_extrapolated_values_backwards)
