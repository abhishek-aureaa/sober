def SequenceFound(intArr):
    sequence = False
    
    for i in range (0, len(intArr)-2):
        if(intArr[i] == 1):
            if(intArr[i+1] == 3):
                if(intArr[i+2] == 4):
                    sequence = True
                    break
                
    return sequence

intArr = [7,7,9,9,0,1,3,4,2,2,3,3]
print("sequence of 1,3,4 found :",str(SequenceFound(intArr)))