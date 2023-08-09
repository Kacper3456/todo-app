import functions
import PySimpleGUI as sg

label=sg.Text("Type in to-do: ")
add_button=sg.Button("Add")
input_box=sg.InputText(tooltip="Enter a todo",key='todo')
window=sg.Window('My Todo App',
                 layout=[[label,input_box,add_button]],
                 font=('Helvetica',20))
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todos=values['todo']+'\n'
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()

