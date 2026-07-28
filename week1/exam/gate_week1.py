text = """The ocean covers most of the planet, yet the ocean remains largely unmapped.
Every year new species are found in the deep ocean, and every year the map of
the deep changes. Scientists study the ocean because the ocean shapes the
weather, the climate, and the food that people eat. Understanding the ocean is
understanding the planet."""
text_banned = "the, is, a, of, and, to, in, it, that, are, yet, most"
words = text.lower().split()
word_count = {}
words_cleaned = [word.strip(",.") for word in words]
stop_words = set(text_banned.split(", "))
for word in words_cleaned:
    if word in stop_words:
        continue
    word_count[word] = word_count.get(word, 0) + 1
word_count_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in word_count_sorted[:10]:
    print(f"{word}: {count}")
number = len(word_count)
print(f"去重后共有{number}个不同的词")

