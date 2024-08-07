import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w'):
        pass

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My Todo App")

print(todos)

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        print(todos)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()


st.text_input(label="", placeholder="Add a new todo..",
              on_change=add_todo,key='new_todo')

