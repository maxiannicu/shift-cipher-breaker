# Shift cipher breaker

## About

This breaker is a flexible as it depends upon a dictionary and not a language.
There is a dictionary with data in file `words_dictionary.json`. This dictionary is used in both methods for decryption. This dictionary can be replaced to be in different language.

## Methods

### Simple Dictionary attack

This method step by step shifts with one character to the right. After creating new message, it is checked how many words exists in our dictionary. In case we have 100% of words, matching our dictionary, we stop searching for solution.

### Frequency analysis

This method analyzes the dictionary and finds the frequency. After that, it also analyses input frequency. After that algorithm is trying to find shift number by comparing order of most freqvent letter in dictionary and input. In long messages, complexity of this will be `O(1)`. Although this algorithm will not necessearily find shift from one step.

## Decrypted messages

### Deadline

```text
Choose decrypting method
1 Dictionary attack
2 Frequency analysis
Enter option number : 1
------
Match: 100%
Shift: 7 characters
Decryption: hi guys the deadline for this laboratory is the twentieth of december i would like to wish you good luck with it and have a nice life
```

### First message

```text
Match: 95%
Shift: 16 characters
Decryption: maximus: my name is maximus decimus meridius, commander of the armies of the north, general of the felix legions, loyal servant to the true emperor, marcus aurelius. father to a murdered son, husband to a murdered wife. and i will have my vengeance, in this life or the next.
```

This result is not 100% because it contains personal names which are not present in dictionary.

### Second message

```text
Choose decrypting method
1 Dictionary attack
2 Frequency analysis
Enter option number : 2
Analyzing  data  frequency...
e  :  376459
i  :  313008
a  :  295794
o  :  251598
n  :  251433
s  :  250281
r  :  246146
t  :  230895
l  :  194915
c  :  152981
u  :  131495
p  :  113662
d  :  113188
m  :  105203
h  :  92372
g  :  82626
y  :  70579
b  :  63940
f  :  39238
v  :  33075
k  :  26814
w  :  22408
z  :  14758
x  :  10493
q  :  5883
j  :  5458
Done.
Analyzing  input  frequency...
x  :  50
m  :  27
h  :  21
k  :  21
l  :  18
g  :  16
t  :  16
b  :  13
w  :  13
a  :  10
f  :  9
z  :  8
r  :  7
y  :  7
e  :  6
i  :  6
v  :  5
u  :  4
o  :  3
n  :  3
q  :  3
p  :  3
d  :  1
c  :  0
j  :  0
s  :  0
Done.
------
Match: 100%
Shift: 7 characters
Decryption: every plan is to be considered, every expedient tried and every method taken before matters are brought to this last extremity. good officers decline general engagements where the odds are too great, and prefer the employment of stratagem and finesse to destroy the enemy as much as possible without exposing their own forces.
```

### Third message

```text
Choose decrypting method
1 Dictionary attack
2 Frequency analysis
Enter option number : 2
Analyzing  data  frequency...
e  :  376459
i  :  313008
a  :  295794
o  :  251598
n  :  251433
s  :  250281
r  :  246146
t  :  230895
l  :  194915
c  :  152981
u  :  131495
p  :  113662
d  :  113188
m  :  105203
h  :  92372
g  :  82626
y  :  70579
b  :  63940
f  :  39238
v  :  33075
k  :  26814
w  :  22408
z  :  14758
x  :  10493
q  :  5883
j  :  5458
Done.
Analyzing  input  frequency...
j  :  44
w  :  20
y  :  20
f  :  19
s  :  18
n  :  16
i  :  12
x  :  12
q  :  11
t  :  11
m  :  10
a  :  8
r  :  8
d  :  6
k  :  6
l  :  6
z  :  5
h  :  4
u  :  3
g  :  2
c  :  1
b  :  1
e  :  0
o  :  0
p  :  0
v  :  0
Done.
------
Match: 100%
Shift: -5 characters
Decryption: my love for the roman empire is undeniably greater than for myself. the greatest empire ever to have existed. i pledge my eternal servitude and i am forever bound to serve it, in life and in death. they have merely given us: roads, central heating, concrete, the calendar, and flushing toilets and sewers.
```

## Conclusion

Shift cipher is very simple and can be easily breaked. I think that dictionary attack works faster in our case as we have at most 27 iterations (letters in alphabet) and don't have a extra work to do. Frequency analysis has a init work to do, analyse of dictionary and input, which is a bit costly. But instead, this is very performant for breaking substitution cipher.