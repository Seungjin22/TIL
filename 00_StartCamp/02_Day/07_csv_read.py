#csv 파일 read의 2가지 방법

#1. split
with open('lunch.csv', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        print(line.strip().split(','))

#2. csv reader
import csv

with open('lunch.csv', 'r', encoding = 'utf-8') as f:
    lines = csv.reader(f)

    for line in lines:
        print(line)