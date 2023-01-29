import csv
import sys


def wgid_filter(ln):
    if ln[0].isdigit():
        return ln[0:2]


def game_filter(ln):
    if len(ln[1]) > 8:
        return ln[0:2]


def file_reader(data):
    for line in list(csv.reader(data))[1:]:
        yield line


if __name__ == "__main__":

    i_file, o_file, filter1, filter2 = (sys.argv[1:] + [None] * 4)[:4]

    with open(i_file) as acc_game:
        accounts = file_reader(acc_game)

        new_data = []
        filter1 = globals()[filter1]

        for acc in accounts:
            filtered = None
            filtered = filter1(acc)

            if filtered is not None:

                if filter2 == "wgid_filter" or filter2 == "game_filter":
                    filtered = globals()[filter2](filtered)
                new_data.append(filtered)

        print(new_data)
        if len(new_data) != 0:
            with open(o_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)
