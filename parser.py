file = open('./sample_1.hl7', 'r')

obj = []
for line in file:
    for i in line.split('|'):
        obj.append(i.split('^'))

hl7_json = {}

for i in obj:
    hl7_json[i[0]] = i

print(hl7_json)
