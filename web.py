import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"] + '\n'
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My To-do App")
st.write("This app will help increase your productivity :D")


st.checkbox("Buy grocery")
st.checkbox("Throw the groceries")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "", placeholder = "Add new todo: ",
              on_change = add_todo, key = 'new_todo')