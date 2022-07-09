# trie = {'a': {'n': {'d': {'end': True}, 'o': {'end': True}}, 'p': {
#     'p': {'l': {'e': {'end': True}}}}}, 'b': {'a': {'end': True}}}
# trie = {'a': {}}
trie = {}


def split(text):
    return [i for i in text]


def insert(text):
    split_text = split(text)
    current_level = trie
    for index, i in enumerate(split_text):
        if i not in current_level.keys():
            current_level[i] = {}

        if index == len(split_text)-1:
            current_level[i]['end'] = True

        current_level = current_level[i]


# Enter words
insert('apple')
insert('app')
print(trie)


def search(text):
    split_text = split(text)
    current_level = trie
    for index, i in enumerate(split_text):
        if i not in current_level.keys():
            print("Not found")
            break

        if index == len(split_text)-1 and 'end' in current_level[i].keys():
            print("Word found")
            break

        if index == len(split_text)-1 and 'end' not in current_level[i].keys():
            print("Word not found")
            break

        current_level = current_level[i]


# Find words
search("apples")
