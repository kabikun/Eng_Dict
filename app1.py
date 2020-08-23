# import json
# from difflib import get_close_matches

# data=json.load(open("App#1/data.json"))

# def searchWord(w):
#     # notes #1 data=json.load(open("data.json")) <------move this out of the fuction above
#     w=w.lower()
#     if w  in data:
#         return data[w]
#         #return "\n".join(data[w])
#     elif len(get_close_matches(w, data.keys()))>0:

#         yn=input("did you mean %s instead ? Please Type 'Y' for Yes, 'N' for No: "  %get_close_matches( w, data.keys())[0])  #cloest word is at first position[0]
#         if yn=="Y":
#             return data[get_close_matches(w, data.keys())[0]]
#             #return "\n".join(data[get_close_matches(w, data.keys())[0]])
#         elif yn=="N":
#             return "please try another word"
#         else:
#             return "please enter 'Y' or 'N' only"        

#     else:
#         return "please try another word" # use return instead print     
   

# user_input=input("Give me a word:") #global variable careful where to put user_input

# #print(searchWord(user_input))

# output=searchWord(user_input) # or use the "\n".join() method
# if type(output)==list:
#     for item in output:
#         print(item)

# else:
#     print(output)    
  
###########################################################################################################

import json

from difflib import get_close_matches

data=json.load(open("App#1/data.json"))

def searchWord(w):
    #w=w.lower()

    if w.lower() in data: 
        return data[w.lower()]
        #return "\n".join(data[w])
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]    
    elif len(get_close_matches(w, data.keys()))>0:
        c=input("Did you mean %s instad ? type 'Y' for Yes and 'N' for No: " %get_close_matches(w, data.keys())[0])  # return the closest guess at [0]
        if c.lower()=="y":
            return data[get_close_matches(w, data.keys())[0]] 
        elif c.lower()=="n": 
            return "Ok...Word not found"
        else:
            while True:   # improvement: keep asking for Y or N if the input is not Y or N
                if c.lower()=="y":
                    return data[get_close_matches(w, data.keys())[0]]
                elif c.lower()=="n": 
                    return "Ok...Word not found"
                else:
                    c=input("Type'Y' or 'N'. Type 'End' to stop the program: " )
                    if c.lower()=="end":
                        return "Program ended, plese try next time"
                               
    else: 
        return "Sorry...Word not found"

user_input=input("Which definition you looking for: ")
output=searchWord(user_input)  

if type(output)==list:
    for item in output:
        print(item)

else:
    print(output)