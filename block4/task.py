import csv
import os
import sys


def wgid_filter(wgid: str, ln: list) -> list:
    if ln[0].find(wgid) != -1:
        return ln[0:2]


def game_filter(game: str, ln: list) -> list:
    if ln[1].find(game) != -1:
        return ln[0:2]


def initial_filter(info: list, filter1: str = None, filter2: str = None) -> list:
    filtered = None

    if filter1.isdigit():
        filtered = wgid_filter(filter1, info)
    else:
        filtered = game_filter(filter1, info)

    if filter2 is not None and filtered is not None:
        if filter2.isdigit():
            filtered = wgid_filter(filter2, info)
        else:
            filtered = game_filter(filter2, info)

    return filtered


def file_reader(i_file):
    if os.path.isfile(i_file):
        with open(i_file) as acc_game:
            for line in csv.reader(acc_game):
                yield line
    else:
        return None


def lets_filter(i_file, filter1: str = None, filter2: str = None) -> list:

    if filter1 is None:
        return None

    info = file_reader(i_file)

    # doesn't catch an error
    # try:
    #     next(info)
    # except FileExistsError:
    #     print("Doesn't exist")
    #     return None

    new_data = []

    for line in info:
        filtered = None
        filtered = initial_filter(line, filter1, filter2)

        if filtered is not None:
            new_data.append(filtered)

    return new_data


if __name__ == "__main__":

    inp, outp, filt1, filt2 = (sys.argv[1:] + [None] * 4)[:4]
    data = lets_filter(inp, filt1, filt2)

    if data is not None:
        with open(outp, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
