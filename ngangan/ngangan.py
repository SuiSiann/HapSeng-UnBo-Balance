import csv

with open(
        '名姓字表 - 字姓.csv') as tong:
        reader = csv.reader(tong)
        next(reader, None)
        senn = []
        for pit in reader:
            senn.append(pit[2])


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



print(senn[0], 'X', ngangan_w[0])
print(senn[1], ngangan_w[1], 'X')
print('X', ngangan_w[2])
print(ngangan_w[3], 'X')
print(senn[2], 'X', ngangan_w[4])
print(senn[3], ngangan_w[5], 'X')
print('X', ngangan_w[6])
print(ngangan_w[7], 'X')
