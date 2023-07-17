from IPython.display import clear_output
#THE TASKLIST CLASS
class TaskList():
    def __init__(self):
        self.task_list = []




    
#DISPLAY TASKS
    def display_task(self):
        print('Here are your current tasks:')
        print(self.task_list)



    
#ADD TASKS
    def task_choice(self):
        choice = input("What task would you like to add? (Enter 'stop' to finish): ")
        while choice.lower() != 'stop':
            self.task_list.append(choice)
            choice = input("What task would you like to add? (Enter 'stop' to finish): ")




    
        
#TO REMOVE TASKS
    def task_removal(self):
        choice = input("What task would you like to remove? (Enter 'skip' to leave list as it is): ")
        while choice.lower() != 'skip':
            try:
                self.task_list.remove(choice)
            except ValueError:
                print('This task is not in the list. Please enter a valid task!')
            choice = input("What task would you like to remove? (Enter 'skip' to leave list as it is): ")
        return choice





#THE OPTIONS PAGE TO DETERMINE WHAT ACTION I WANT TO MAKE   
class Options(TaskList):
    def __init__(self):
        #SUPER GIVES ME ACCESS TO THE METHODS AND PROPS OF THE TASKLIST CLASS
        super().__init__()

#TO RUN THE OPTIONS
    def run_options(self):
        while True:
            
            option = input(
                'What do you want to do?\n1. View Tasks\n2. Add Task\n3. Remove Tasks\n4. End Program\n')
            if option == '1':
                self.display_task()
            elif option == '2':
                self.task_choice()
            elif option == '3':
                self.task_removal()
            elif option == '4':
                self.taskon_choice()
                break
                clear_output()
            else:
                print("Invalid option. Please try again.")






# Create an Options object TO LINK BOTH TASKLIST AND OPTIONS TOGETHER
options_obj = Options()
options_obj.run_options()

print("Task management is complete.")
