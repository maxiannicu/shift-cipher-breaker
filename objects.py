class result:
    def __init__(self, percentage, shift, decrypted_sentence):
        self.percentage = percentage
        self.shift = shift
        self.decrypted_sentence = decrypted_sentence

    def __cmp__(self, other):
        return self.percentage - other.percentage

    def __str__(self):
        return "Match: {0}%\nShift: {1} characters\nDecryption: {2}".format(self.percentage,
                                                                            self.shift,
                                                                            self.decrypted_sentence)
