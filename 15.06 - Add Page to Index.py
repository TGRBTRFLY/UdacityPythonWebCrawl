# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    # not found, add a new entry
    index.append([keyword, [url]])


def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []


def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)


index = []

# add_page_to_index(index,'fake.text',"This is a test")
# print index
# >>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
# >>> ['test',['fake.text']]]

add_page_to_index(index, 'http://dilbert.com',
                  """
                  Another strategy is to ignore the fact that you are slowly killing yourself by not sleeping and exercising enough. That frees up several hours a day. The only downside is that you get fat and die. --- Scott Adams on Time Management """)

add_page_to_index(index, 'http://randy.pausch',
                  """
                  Good judgment comes from experience, experience comes from bad judgment. If things aren't going well it probably means you are learning a lot and things will go better later. --- Randy Pausch """)

print
index

# query - to find the occurences of a word
print
lookup(index, 'you')
