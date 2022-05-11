import csv

with open(
        '名姓字表 - 字姓.csv') as tong:
        reader = csv.reader(tong)
        next(reader, None)
        senn_dict = {}
        for pit in reader:
                print(pit[2])



with open(
        '名姓字表 - 人名.csv') as tong:
        reader = csv.reader(tong)
        next(reader, None)
        senn_dict = {}
        ngangan = []
        for pit in reader:
            if '(文)' in pit[1]:
                ngangan.append(pit[:2])
        print(ngangan)
