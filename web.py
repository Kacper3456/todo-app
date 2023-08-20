import streamlit as st
import functions

todos=functions.get_todos()
def add_todo():
    todo=st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My to-do app ")
st.subheader("this is my todo app")
st.write("this is my app to increase productivity")


todos=functions.get_todos()

for todo in todos:
    st.checkbox(todo)
st.text_input(label=" ",placeholder="Add a new todo",on_change=add_todo,key="new_todo")
print("hello")


st.session_state