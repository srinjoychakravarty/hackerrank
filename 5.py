def overlapPrefix(l):
    length = len(l) 
    complete_array = [] 
    for i in range(length):
        total = 0 
        string = l[i] 
        characters_in_string = len(string) 
    
        for j in range(characters_in_string):
            suffix = string[j:]
            length_of_suffix = len(suffix) 
            overlap = 0 
    
            for k in range(length_of_suffix):
                if(string[k] == suffix[k]):
                    overlap = overlap + 1
                else:
                    break 
            total = total + overlap 
            
        complete_array.append(total) 
      

    return complete_array 

if __name__ == '__main__':
    print(overlapPrefix(["ababaa"]))
