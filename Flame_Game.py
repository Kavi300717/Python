def remove_match_char(list1, list2):

    for i in range(len(list1)):
        for j in range(len(list2)):

            #if common character is found hen remove that character and return list of concatenated list with True Flag
            if list1[i] == list2[j]:
                c = list1[i]

                #remove character from list
                list1.remove(c)
                list2.remove(c)

                list3 = list1 + ["*"] + list2
                
                #retrun the concatenated list withTrue flag
                return [list3, True]
            
    list3 = list1 + ["*"] + list2
    return [list3, False]

if __name__ == "__main__":
    #Take first Name
    p1 = input("Player 1 Name : ")

    #Converting all the letter into lower case
    p1 = p1.lower()

    #replace any empty space with empty strng
    p1.replace("", "")

    #making the list of letters or characters
    p1_list = lisst(p1)

    #Take 2nd name
    p2 = input("Player 2 Name : ")
    p2 = p2.lower()
    p2.replace("", "")
    p2_list = list(p2)

    proceed = True

    while proceed:

        #function calling and store return value
        ret_list = remove_match_char(p1_list, p2_list)

        #Taking put the concatenated list from th retrun list 
        con_list = ret_list[0]

        #taking out the flag value from the retrun list
        proceed = ret_list[1]

        #finding the index of "*"
        star_index = con_list.index("*")

        #Slicing the list all the character before * will be store in p1_list
        p1_list = con_list[: star_index]

        #All character before * will be store in p2_list
        p2_list = con_list[star_index + 1:]

    #Count total remaining character
    cont = len(p1_list) + len(p2_list)

    #List of flame acronym
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Silings"]

    while len(result) > 1:
        split_index = (count % len(result) - 1)

        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[: split_index]

            result = right + left
        else:
            result = result[: len(result) - 1]
print("relationship status :", result[0])

