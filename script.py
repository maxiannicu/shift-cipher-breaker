import utils
import objects

search_string = utils.read_input_sentence()

result = objects.result(-1, -1, "No decryption")


def check_decoding(decoded, shift_used):
    global result
    percentage = utils.get_sentence_percentage(decoded)
    current_result = objects.result(percentage, shift_used, decoded)

    if result < current_result:
        result = current_result


def check_with_shift(i):
    decoded = ""
    for c in search_string:
        if c.isalpha():
            decoded = decoded + utils.get_shifted_char(c, i)
        else:
            decoded = decoded + c

    check_decoding(decoded, i)


def dictionary_attack():
    global result
    for i in range(1, ord('z') - ord('a')):
        check_with_shift(i)
        if result.percentage == 100:
            break


def frequency_analysis():
    global result
    words = utils.get_words(search_string)
    frequencies = utils.get_frequencies()
    input_frequencies = utils.get_frequencies(words, "input")

    input_first_letter = input_frequencies[0]

    for i in frequencies:
        delta = ord(input_first_letter[0]) - ord(i[0])
        check_with_shift(delta)
        if result.percentage == 100:
            break


print "Choose decrypting method"
print 1, "Dictionary attack"
print 2, "Frequency analysis"

option = eval(raw_input("Enter option number : "))

if option == 1:
    dictionary_attack()
if option == 2:
    frequency_analysis()

print "------"
print result
