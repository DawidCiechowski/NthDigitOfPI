def find_nth_integer(n):
        f = open("PI.txt", "r")
        nth = 0
        chars = 0
        with f as fileObj:
                for line in fileObj:
                        for ch in line:
                                nth += 1
                                if(nth == n):
                                        if(nth % 10 == 1):
                                                print (str(nth).strip() + "st digit of PI:", ch)
                                        elif(nth % 10 == 2):
                                                print (str(nth).strip() + "nd digit of PI:", ch)
                                        elif(nth % 10 == 3):
                                                print (str(nth).strip() + "rd digit of PI:", ch)
                                        else:
                                                print(str(nth).strip() + "th digit of PI:", ch)

       
find_nth_integer(999954)