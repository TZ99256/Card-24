'''
Enter any four numbers, it will tell you a mathematical way to make it equal to 24
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
nlist = [num1,num2,num3,num4]
symbols = ['+','-','*','/']


def mathop(num1,num2,symbol):
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    elif symbol == '/':
        return num1/num2
    else:
        return num1*num2

def permutation(numlist):
    '''
    this function will return the permutation of a given list
    '''
    if len(numlist) == 1:
        return [numlist]
    total = []
    for i in range(0, len(numlist)):
        newlist = numlist[:i] + numlist[i+1:]
        for j in permutation(newlist):
            product = [numlist[i]] + j
            total.append(product)
    return total

def possible24combo(combolist):
    all_list = []
    def singlelist(list):
        final_list = []
        for s1 in symbols:
            for s2 in symbols:
                for s3 in symbols:
                    new_list = [list[0]] + [s1] + [list[1]] + [s2] + [list[2]] + [s3] + [list[3]]
                    final_list.append(new_list)
        return final_list
    for l in combolist:
        all_list = all_list + singlelist(l)
    return all_list

def calculate_sum(list):
    sum1 = mathop(list[0],list[2],list[1])
    sum2 = mathop(sum1,list[4],list[3])
    sum3 = mathop(sum2,list[6], list[5])
    return sum3

def final(nlist):
    all_permutation_num = permutation(nlist)
    allcombo = possible24combo(all_permutation_num)
    for i in allcombo:
        if calculate_sum(i) == 24:
            print(i)
print(final(nlist))
        




                                    
                                    


