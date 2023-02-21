import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    # robi zmienną, żeby uaktualniać dodane przez kogośtodo do listy
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
# to subtytuły
st.write("This app is to increase your productivity")
# to dłuższy tekst

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
# to pozwala na usuniecie tylko tego z listy, gdzie był kliknięty checkbox
#potem usune też z całości - dlatego del
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
# ten key identyfy that textinput(st.text_input) widget
# puste okno, a placeholder to podpowiedź co w oknie wpisac