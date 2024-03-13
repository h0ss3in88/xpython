from array import array

number_array = array('i', [10,125,167,188,199,350])

print(number_array)
print(len(number_array))
print(number_array[2])
for number in number_array :
    print(number)

def calculateSumOfElements(arr) -> None :
    total_sum = 0
    for index,val in enumerate(arr) :
        if(index < len(arr)) :
            total_sum += val
    print(total_sum)            

an_other_array = array('i',[1,2,3,4,5])
calculateSumOfElements(number_array)
calculateSumOfElements(an_other_array)