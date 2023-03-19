# 9. Write a function swap_element that contains two args which will be the position of 
# elements present in the list. The function must swap the elements present in those 
# positions. 
# Input: [1,2,3,4,5,6,7,8] function: swap_element(arg1, arg2)

def function(arg1,arg2):
    if(arg1<=len(input_)-1 and arg2<=len(input_)-1)  :
        #  0<7   or   4<7
         if(arg1>=0 and arg2>=0):
               input_[arg1],input_[arg2]=input_[arg2],input_[arg1]
               print(input_)
         else:
            print("didnt swap because one of the index position is  low")
    else:
        print("didnt swap because one of the index position is high" )


input_=[1,2,3,4,5,6,7,8]
pos1=int(input())
pos2=int(input())
print(input_)
function(pos1, pos2)

#--------------------------------------------------------------------------

# def func_(list_, arg1, arg2):
#     list_[pos1], list_[pos2] = list_[pos2], list_[pos1]
#     return list_

# list_=[1,2,3,4,5,6,7,8]
# pos1=int(input())
# pos2=int(input())
# print(list_)
# print(func_(list_,pos1, pos2))
