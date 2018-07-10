# # \t 的个数 决定了 上一层是第几层
# dir
#    上一层为0，当前层长度为3
# \tsubdir1
#    上一层为1， 因为有一个tab，当前层长度为7
# \tsubdir2\n
# 	上一层为1，因为有一个tab，当前层长度为7
# \t\tfile.ext
# 	上一层为2，当前层长度为8
# 总长度为 3+7+8+2(2为两个slash的长度)，所以是20

# 因为前面的长度，后面不用，所以可以覆盖
# 比方说 subdir1/abcd.txt 长度大于
# subdir2/ab.txt, 但是subdir1的item一定会先于subdir2被访问
def lentghLongestPath(input):
	maxlen = 0
	pathlen = {0: 0}
	for line in input.splitlines():
		name = line.lstrip('\t')
		depth = len(line) - len(name)
		if '.' in name:
			maxlen = max(maxlen, pathlen[depth] + len(name))
		else:
			pathlen[depth+1] = pathlen[depth] + len(name) + 1
	return maxlen


print lentghLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")