def print_sum(num_sum, num_list, num):
    i = 0
    num_length = len(str(num))
    while i < (len(num_list) - 1):
        temp_str = "{0: >" + str(num_length) + "} + "
        print (temp_str.format(num_list[i]), end = "")
        i+=1
    temp_str = "{0: >" + str(num_length) + "} = {1: >" + str(num_length) + "}"
    print (temp_str.format(num_list[i], num_sum), end = "\n")

def test_keith(num, num_list):
    num_sum = 0
    for n in num_list:
        num_sum += n
    print_sum(num_sum, num_list, num)
    if(num_sum > num):
        print("not a keith: " + str(num_sum) + " > " + str(num))
    elif(num_sum == num):
        print("keith: " + str(num_sum))
    else:
        new_num_list = []
        i = 1
        while i < len(num_list):
            new_num_list.append(num_list[i])
            i+=1
        new_num_list.append(num_sum)
        test_keith(num, new_num_list)    

def __main__():
    choice = 1
    while choice != 0:
        num = int(input("Please enter an integer: "))
        print()
        num_str = str(num)
        num_list = []
        for c in num_str:
            num_list.append(int(c))
        test_keith(num,num_list)   
        choice = int(input("\nWould you like to enter anohter number? (1 - yes, 0 - no) "))
        print()

__main__()
