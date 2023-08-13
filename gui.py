import functions
import PySimpleGUI as sg

label=sg.Text("Type in to-do: ")
add_button=sg.Button("Add")
input_box=sg.InputText(tooltip="Enter a todo",key='todo')
list_box=sg.Listbox(values=functions.get_todos(),key='todos',
                    enable_events=True,size=[45,10])
edit_button=sg.Button("Edit")
complete_button=sg.Button("complete")
exit_button=sg.Button("exit")
window=sg.Window('My Todo App',
                 layout=[[label,input_box,add_button],[list_box,edit_button,complete_button],[exit_button]],
                 font=('Helvetica',10))
while True:
    event,values=window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todos=values['todo']+'\n'
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo=values['todo']

            todos=functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos(todos)
            print(new_todo+todo_to_edit)
            window['todos'].update(values=todos)
        case 'complete':
            todo_to_complete=values['todos'][0]
            todos=functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value=' ')
        case 'exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'])
        case sg.WIN_CLOSED:
            break
window.close()

