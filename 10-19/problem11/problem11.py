"""
PROBLEM #11 [MEDIUM]

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string `de` and the set of strings `[dog, deer, deal]`, return `[deer, deal]`.

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


class Trie:
    """
    Digital Tree, also known as Trie.
    Store the leading char, and a map of <key, Trie> to store subsequent chars.

    To store "hello" we will do it by:
            ""
            |
            h
            |
            e
            |
            l
            |
            l
            |
            o
    Then to add "how" we would have:
            ""
            |
            h
            | \
            e  o
            |  |
            l  w
            |
            l
            |
            o
    After adding "here" we would have:
             ""
             |
             h
           /   \
          e     o
         / \    |
        l   r   w
        |   |
        l   e
        |
        o

    So to autocomplete any prefix, process char by char and fetch corresponding sub-Trie:
    > autocomplete("he") would return everything under ""/h/e:
            ""
            |
            h
            /   
         e << everything under this needs to be returned    
        / \    
       l   r 
       |   |
       l   e
       |
       o
    """
    def __init__(self) -> None:
        self.children: {str: [Trie]} = {}
        self.value = ""
    
    def build(self, dictionary: [str]) -> None:
        for word in dictionary:
            self.add(word)

    def add(self, word: str) -> None:
        if not word:
            return
        
        letter: str = word[0]
        if letter not in self.children:
            self.children[letter] = Trie()
            self.children[letter].value = letter
        
        self.children[letter].add(word[1:])

    def autocomplete(self, word: str) -> [str]:
        letter: str = word[0] if word else ""
        
        if letter and letter not in self.children:
            return []
        elif letter in self.children:
            return [self.value + result for result in self.children[letter].autocomplete(word[1:])]
        else:
            results: [str] = []
            for key in self.children:
                results.extend(self.children[key].autocomplete(""))
            
            if not self.children:
                return [self.value]
            else:
                return [self.value + result for result in results]


if __name__ == "__main__":
    trie: Trie = Trie()
    trie.build(dictionary=["dog", "deer", "deal", "donut"])

    assert trie.autocomplete("de") == ["deer", "deal"]
    assert trie.autocomplete("") == ["dog", "donut", "deer", "deal"]
    assert trie.autocomplete("a") == []
    assert trie.autocomplete("donut") == ["donut"]
    assert trie.autocomplete("donuts") == []

    print("Successfully tested.")
