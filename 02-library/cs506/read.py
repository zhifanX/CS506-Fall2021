def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    f = open(csv_file_path, "r")
    lines = f.readlines()
    matrix = []
    for line in lines:
        matrix.append([line])

    return matrix

