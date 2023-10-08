# terminal: pip freeze > requirements.txt
# this is a file which will be uploaded to the server so the server will know all the python libs that
# are needed in order to run the web app
import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    # get the to-do from the input field
    # session state is a type that is similar to a dict: st.session_state
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My todo app")
st.subheader("This is my todo webapp")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):        # todo bugfix
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        functions.write_todos(todos)
        # del removes the checkbox after its checked
        del st.session_state[todo]
        st.rerun()

# on_change is a callback function
st.text_input(label="", placeholder="Type a new todo...",
              on_change=add_todo, key="new_todo")
# print("Hello")
# st.session_state
