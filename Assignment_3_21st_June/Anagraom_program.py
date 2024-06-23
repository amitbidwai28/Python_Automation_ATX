def check_anagram(anagram_1, anagram_2):
    if len(anagram_1) == len(anagram_2):

        # sort the strings
        sorted_str1 = sorted(anagram_1)
        print(sorted_str1)
        sorted_str2 = sorted(anagram_2)
        print(sorted_str2)

        # if sorted char arrays are same
        if sorted_str1 == sorted_str2:
            print(anagram_1 + " and " + anagram_2 + " are anagram.")
        else:
            print(anagram_1 + " and " + anagram_2 + " are not anagram.")

    else:
        print(anagram_1 + " and " + anagram_2 + " are not anagram.")


str1_anagram = input("Enter the first string: ").lower()
str2_anagram = input("Enter the second string: ").lower()
check_anagram(str1_anagram, str2_anagram)
