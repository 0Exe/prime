def prime(num:int, show:bool = True, sf:bool = True):
    if num == 2:
        print(num)
        if not sf:
            return True
    elif num % 2 == 0:
        return False
    elif num == 5:
        print(num)
        if not sf:
            return True
    elif num%10 == 5 or num%10 == 0:
        return False
    else:
        counter = 0 
        for i in range(1, round(num/2)):
            if num % i == 0:
                counter += 1
                if counter > 1:
                    return False
                else:
                    if show and i != 1:
                        print(i)
        if counter == 1:
            print(num)
            if not sf:
                return True
        else:
            return False
