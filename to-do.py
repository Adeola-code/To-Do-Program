from IPython.display import clear_output
clear_output()

#EMPTY TASKLIST AT FIRST
task_list =[]
def display_task(task_list):
    print('Here are your current tasks')
    print(task_list)
# ADD TASKS
def task_choice():
    choice=input("What task would you like to add?: (Enter 'stop' to finish) ")
    while choice.lower() != 'stop':
        #As long as 'stop' is not typed, keep running
        task_list.append(choice)
        choice=input("What task would you like to add?: (Enter 'stop' to finish) ")
        
    clear_output()
    
#REMOVE TASKS
def task_removal():
    choice=input("What task would you like to remove?: (Enter 'skip' to leave list as it is) ")
    #IF SKIP IS TYPED, DONT CHANGE ANYTHING
    while choice.lower() != 'skip':
        #TO CHECK IF THE TASK YOU WANT TO REMOVE IS IN THE LIST OR ELSE IT'LL DISPLAY AN ERROR MESSAGE
        try:
            task_list.remove(choice)
        except ValueError:
            print('This task is not in the list. Please enter a valid task!')
        choice=input("What task would you like to remove?: (Enter 'skip' to leave list as it is) ")
    return(choice)
    
#CONTINUE OR STOP
def taskon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Would you like to add more tasks? Y or N ")

        if choice not in ['Y', 'N']:
            clear_output()

            print("Oops! I didn't get that. Please make sure to choose Y or N")

    if choice == "Y":
        #Still wanna add more tasks
        return True
    else:
        #No more tasks
        return False

    #OMO! TO SUM EVERYTHING AND KEEP IT RUNNING ALTOGETHER SHA
taskon= True

#First Task list

while taskon:

    #clear past output and show list
    clear_output()
    display_task(task_list)

    #Choose Task to add
    task_choice()


    clear_output()
    display_task(task_list)

    #choose to remove task 
    task_removal()

    #clear screen and show new task list
    clear_output()
    display_task(task_list)

    #To keep on adding
    taskon= taskon_choice()



