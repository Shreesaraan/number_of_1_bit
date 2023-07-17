def number_of_1_bit(number):
    count=0
    while number:
        number&=number-1
        count+=1
    return count


number=int(input("Enter the Number : "))
print(number_of_1_bit(number))