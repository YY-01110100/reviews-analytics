data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('档案读取完了, 总共有', len(data), '笔资料')


sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)
print('每一笔留言的平均长度为', sum_len/len(data), '个字。')

