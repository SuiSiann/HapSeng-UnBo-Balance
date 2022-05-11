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
        ngangan_w = []
        ngangan_p = []
        for pit in reader:
            if '(文)' in pit[1]:
                ngangan_w.append(pit[0])
            if '(白)' in pit[1] or '(不標)' in pit[1]:
                ngangan_p.append(pit[0])
        print(ngangan_w, ngangan_p)

