import csv
import re
from kesi.susia.kongke import thiah
from itertools import chain

CENTRAL_VOWELS = [
    'er', 'erh', 'erm', 'ere', 'ereh',  # 泉　鍋
    'ir', 'irh', 'irp', 'irt', 'irk', 'irm', 'irn', 'irng', 'irinn',
]

LOMAJI_PATTERN = re.compile(r'(.+)\(.\)')
ALL_DIGITS = re.compile(r'[0-9]+')

jisenn = '名姓字表 - 字姓.csv'
langmia = '名姓字表 - 人名.csv'


def thak_jipio(*paths):
    for path in paths:
        with open(path, 'r') as jipio_csvfile:
            reader = csv.reader(jipio_csvfile)
            chiau_un_pun_hanji = {}
            for row in reader:
                hanji = row[0]
                if len(hanji) > 1:
                    continue
                for col in row[1:]:
                    try:
                        lomaji = LOMAJI_PATTERN.match(col).group(1)
                    except AttributeError:
                        break
                    un = thiah(lomaji)[1]
                    if un in CENTRAL_VOWELS:
                        chiau_un_pun_hanji.setdefault(un, []).append(hanji)
    return chiau_un_pun_hanji


def thak_bunko():
    chiau_un_pun_hanji = thak_jipio(jisenn, langmia)
    with open('頭一批.txt') as text:
        with open('逐句韻母統計.csv', 'w') as csvfile:
            header = list(chain(['ku'], CENTRAL_VOWELS))
            writer = csv.DictWriter(csvfile, fieldnames=header)
            print(writer.fieldnames)
            writer.writeheader()
            for line in text:
                if line.startswith('--- 分類'):
                    continue
                elif not line.strip():
                    continue
                elif ALL_DIGITS.fullmatch(line.strip()):
                    continue
                line_copy = line
                for ji in ['仔', '予', '會使', '袂使']:
                    line = line.replace(ji, '')
                d = {'ku': line_copy}
                for k, v in chiau_un_pun_hanji.items():
                    un_count = 0
                    for ji in v:
                        un_count += line.count(ji)
                    d[k] = un_count
                writer.writerow(d)


if __name__ == '__main__':
    thak_bunko()
