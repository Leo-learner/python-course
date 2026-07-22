#1. 准备文本
#2. 转小写、切分成词列表
#3. 遍历列表，用dict记账
#4. 排序，打印前十
text = "Python is simple. Python is powerful. Learning Python is fun and practical. In data science, Python is the first choice. When learning to code, simple solutions are often the best. Writing simple code is a skill that every Python developer loves."
words = text.lower().split()
word_count = {}
for word in words:
    word = word.strip(",.")
    word_count[word] = word_count.get(word, 0) + 1

sorted_word_count = sorted(word_count.items(), key=lambda x: x[1],reverse=True)
for word, count in sorted_word_count[:10]:
    print(f"{word}: {count}")
