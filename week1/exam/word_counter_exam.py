text = "Learning data science is not just about writing code. It is also about asking questions, exploring data, and discovering hidden patterns. Python code is often the bridge between raw data and valuable insights. Data science is a journey of continuous learning, and every line of code tells a story about the data."
words = text.lower().split()
word_count = {}
words_cleaned = [word.strip(",.") for word in words]
for word in words_cleaned:
    word_count[word] = word_count.get(word, 0) + 1
word_count_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse = True)
for word, count in word_count_sorted[:10]:
    print(f"{word} {count}")


