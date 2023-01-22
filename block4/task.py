import csv
import sys

'''
files = []

for line in sys.stdin:
   if 'Exit' == line.rstrip():
       break
   files.append(line.rstrip())
'''

files = ["account_game.csv", "filtered_data.csv", "wgid_filter", "game_filter"]

input_file = files[0]
output_file = files[1]

with open(input_file) as acc_game:
    data = list(csv.reader(acc_game))


def wgid_filter(lst):
    info_list = [line[0:2] for line in lst[1:] if not line[0].isdigit()]
    return info_list


def game_filter(lst):
    info_list = [line[0:2] for line in lst[1:] if len(line[1]) > 8]
    return info_list


with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    if files[2]:
        new_id_data = wgid_filter(data)
        writer.writerows(new_id_data)
    if files[3]:
        new_game_data = game_filter(data)
        writer.writerows(new_game_data)
