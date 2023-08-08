import functions
import PySimpleGUI as sg

label=sg.Text("Type in to-do: ")
add_button=sg.Button("Add")
input_box=sg.InputText(tooltip="Enter a todo")
window=sg.Window('My Todo App',layout=[[label,input_box,add_button]])
window.read()
window.close()

