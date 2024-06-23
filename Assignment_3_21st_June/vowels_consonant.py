def find_v_w(alpha):
    vowel_lst = []
    consonant_lst = []

    for i in alpha:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowel_lst.append(i)
        else:
            consonant_lst.append(i)
    set_vowel = set(vowel_lst)
    set_consonant = set(consonant_lst)
    print("Vowels are: ", len(set_vowel))
    print("Consonant are: ", len(set_consonant))


lst_tup = input("Enter the string: ").lower()
find_v_w(lst_tup)
