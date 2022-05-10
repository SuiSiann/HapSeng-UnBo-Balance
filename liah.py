import csv
from collections import Counter

all_r_hanji = set()


def thak_hanji(path):
    with open(path, 'r') as tongan:
        for line in tongan:
            all_r_hanji.add(line.strip())


def contains_r_hanji(ku):
    # return any(char in all_r_hanji for char in ku)
    return ''.join([char for char in ku if char in all_r_hanji])


if __name__ == '__main__':
    thak_hanji('langmia-r.txt')
    thak_hanji('jisenn-r.txt')
    with open('例句.csv', 'r') as leku_csvfile:
        with open('kiatko.csv', 'w') as kiatko_csvfile:
            choanpoo_ku = [
                (row['例句'], row['例句標音'], contains_r_hanji(row['例句']))
                for row in csv.DictReader(leku_csvfile)
                if contains_r_hanji(row['例句'])
             ]

            for k, v in Counter(''.join(map(lambda x: x[2], choanpoo_ku))).most_common():
                print(f'{k}: {v}')
            writer = csv.writer(kiatko_csvfile)
            for han, lo, ji in choanpoo_ku:
                writer.writerow([han, lo, ji])
