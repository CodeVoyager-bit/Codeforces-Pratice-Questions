# This is the code

# You were walking down the street and heard a sound. The sound was described by the string 𝑠
#  consisting of lowercase and uppercase Latin characters. Now you want to find out if the sound was a cat meowing.

# For the sound to be a meowing, the string can only contain the letters 'm', 'e', 'o' and 'w', in either uppercase or lowercase. Also:

# string must start with non-empty sequence consisting only of characters 'm' or 'M'
# it must be immediately followed by non-empty sequence consisting only of characters 'e' or 'E'
# it must be immediately followed by non-empty sequence consisting only of characters 'o' or 'O'
# it must be immediately followed by non-empty sequence consisting only of characters 'w' or 'W', this sequence ends the string, after it immediately comes the string end
# For example, strings "meow", "mmmEeOWww", "MeOooOw" describe a meowing, but strings "Mweo", "MeO", "moew", "MmEW", "meowmeow" do not.

# Determine whether the sound you heard was a cat meowing or something else.

# Input
# The first line of input data contains a single integer 𝑡
#  (1≤𝑡≤104
# ) — the number of test cases.

# The description of the test cases follows.

# The first line of each test case contains an integer 𝑛
#  (1≤𝑛≤50
# ) — the length of the string describing the sound.

# The second line of each test case contains a string 𝑠
#  of 𝑛
#  characters. The string describes the sound you heard and consists only of lowercase and uppercase Latin letters.

# Output
# For each test case, output on a separate line:

# YES if the sound was a cat meowing;
# NO otherwise.
# You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be recognized as positive response).

# Example
# InputCopy
# 7
# 4
# meOw
# 14
# mMmeoOoWWWwwwW
# 3
# mew
# 7
# MmeEeUw
# 4
# MEOW
# 6
# MmyaVW
# 5
# meowA
# OutputCopy
# YES
# YES
# NO
# NO
# YES
# NO
# NO
# Note
# In the first test case, the string consists of a sequence of characters 'm', 'e', 'O', 'w', which satisfies the definition of meowing.

# In the second test case, the string consists of a sequence of 3
#  characters 'm' and 'M', one 'e', a sequence of 3
#  characters 'o' and 'O' and a sequence of 7
#  characters 'w' and 'W', which satisfies the definition of meowing.

# In the third test case, the string does not describe a meowing because it lacks a sequence of 'o' or 'O' characters between 'e' and 'w'.

# In the fourth test case, the string contains the character 'U', so it does not describe a meowing.

# This is the code

for i in range(int(input())):
    n=int(input())
    s=input().lower()
    # print(s)
    l=['m','e','o','w',-1]
    j=0
    flag=False
    for i in s:
        if i==l[j]:
            continue
        elif i==l[j+1]:
            j+=1
        else:
            flag=True
            break
    if('m' not in s) or ('e' not in s) or('o' not in s) or('w' not in s)  or flag:
        print('NO')
    else:
        print('YES')
