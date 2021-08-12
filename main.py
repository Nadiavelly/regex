from pprint import pprint
import re
import csv
new = []
res = []
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  data = list(rows)

  for l in data:
    name = l[0]+' '+l[1]+' '+l[2]
    result = re.sub('([А-Я][а-я]+)\s*([А-Я][а-я]+)\s*([А-Я][а-я]+)', '\\1 \\2 \\3', name).strip().split(' ')
    if len(result) < 3:
        result.append('')
    result.append(l[3])
    result.append(l[4])
    phone = re.sub('(\+7|8)?\s*\(?(\d{3})\)?\s*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(?(доб.)*\s*(\d+)*\)?', '+7(\\2)\\3-\\4-\\5 \\6\\7', l[5])
    result.append(phone)
    result.append(l[6])
    new.append(result)
  for l in new:
    for t in new:
      if l[0] == t[0] and l[1] == t[1]:
          if l[2] == '':
            l[2] = t[2]
          else:
            t[2] = l[2]
          if l[3] == '':
            l[3] = t[3]
          else:
            t[3] = l[3]
          if l[4] == '':
            l[4] = t[4]
          else:
            t[4] = l[4]
          if l[5] == '':
            l[5] = t[5]
          else:
            t[5] = l[5]
          if l[6] == '':
            l[6] = t[6]
          else:
            t[6] = l[6]

[res.append(i) for i in new if i not in res]

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(res)





