
def main():   
    
    # COLLECT INPUTS
    collect_input = True
    input_array = []
    
    while (collect_input):
        value = input("")
        if (value == ""):
            collect_input = False
            print("Collected all input")
        else:
            input_array.append(value)
            
    # HANDLE INPUTS
    sum = 0
    
    for code in input_array:
        
        first = None
        last = None
        
        for item in code:
            if (item.isdigit()):
                if (first == None):
                    first = item;
                    last = item;
                else:
                    last = item;
                    
    
        if (first != None and last != None):
            sum += int(str(first) + str(last))
        
    print(sum)
            
if __name__ == "__main__":
    main();