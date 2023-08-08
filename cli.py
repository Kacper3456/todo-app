#from functions import get_todos,write_todos
import functions
import time
now=time.strftime("%b %d, %Y %H:%M:%S")
print("it is "+now)
while True:
    user_action = input("Do you want to add,show,edit,complete or exit? ")
    user_action = user_action.strip()

    if  user_action.startswith("add"):
        todo = user_action[4:]
        #file = open('todos.txt','r')
        #todos = file.readlines()
        #file.close() =
        todos=functions.get_todos()

        todos.append(todo+"\n")

        #file=open('todos.txt','w')
        #file.writelines(todos)
        #file.close()=
        #with open('venv/todos.txt','w') as file:
           # file.writelines(todos)
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()


        # new_todos=[item.strip() for item in todos]

        for index,item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}- {item} "
            print(row)

    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            number=number-1
            todos = functions.get_todos()
            new_todo=input("To what would you like to change this todo? ")
            todos[number]=new_todo+'\n'
            print(todos[number])
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("complete"):
        try:
            with open('venv/todos.txt' , 'r') as file :
                todos=file.readlines()

            number=int(user_action[9:])
            todo_to_remove=todos[number-1].strip('\n')
            todos.pop(number-1)

            message= f"{todo_to_remove} was completed and removed from list.Good job"
            print(message)
            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number ")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("this command is not valid")
print("Goodbye")