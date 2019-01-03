data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('档案读取完了, 总共有', len(data), '笔资料')

print(data[0])


sum_len = 0
for d in data:
	sum_len += len(d)
print('每一笔留言的平均长度为', sum_len/len(data), '个字。')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '笔留言长度小于100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '笔留言提到good')
print(good[0])

good = [d for d in data if 'good' in d] # 上面四行

bad = [ 'bad' in d for d in data]
print(bad)#会印出true 或者 bad

# 文字计数查找
wc = {} #word count
for d in data:
	words = d.split()#split的预设值就是空白键 而且直接使用可以跳过空字串
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('请问你想查什么字：') 
	if word == 'q':
		break
	if word in wc:
		print(word, '出现过的次数为：', wc[word])
	else:
		print('这个字没有出现过哟！')
print('感谢使用本查询功能。')