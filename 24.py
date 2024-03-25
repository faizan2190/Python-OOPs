class String(str):
    def wordCount(self):
        l=self.split(' ')
        return len(l)
sentence=String('I am Maria Waqas, your teacher for the course CS-116')
print(sentence.wordCount())