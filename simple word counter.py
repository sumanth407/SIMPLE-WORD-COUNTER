#this file consist the program for simple word counter.
def word_counter(input):
    filtered_input=input.strip() #removes extra spaces in the begining and ending of the line
    user_input=filtered_input.split() # converts the given string into list which consists words as elements
    return len(user_input) # returns the length of the list which is equal to count of words 
    
client_input=input("Enter a sententance or paragraph:")   # takes the user_input
count=word_counter(client_input) #stores the word count
if count!=0: # if the word count is not equal to 0 
    print(f"the total count of words in the given sentence/paragraph is {count}")
else: # if the word count is equal to  0
    print("you have not not entered any sentence or paragraph\n please enter an valid input")   
     