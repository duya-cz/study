# csv操作
# 写
# with open('爬虫/test.csv', 'w', encoding='utf-8', newline='') as f:
#     f.write('name,age,sex\n')
#     f.write('小王,18,"塑料袋,男"\n')
#     f.write('小张,19,女\n')
#     f.write('小李,20,男\n')

# 读
# with open("爬虫/test.csv","r",encoding="utf-8")as f:
#     for line in f:
#         print(line.strip())


# CSV操作，使用库
import csv
with open('爬虫/test2.csv', 'w', encoding='utf-8', newline='') as f:
    writer=csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader()#写入表头
    writer.writerow({"姓名":"小张","年龄":19,"性别":"女","爱好":"看电影"})
    writer.writerow({"姓名":"小李","年龄":20,"性别":"男","爱好":"看电影"})
# 读
with open('爬虫/test2.csv', 'r', encoding='utf-8') as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row)
        print(row.get('姓名'))#获取这个字典的某一个Key值