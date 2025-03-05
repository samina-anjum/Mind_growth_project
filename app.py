import streamlit as st

# App title
st.title("TO-DO List App")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Sidebar heading
st.sidebar.header("Manage Your Tasks")

# Text input for adding new tasks
new_task = st.sidebar.text_input("Add new task:", placeholder="Enter your task here...")

if st.sidebar.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success("Task successfully added!")
    else:
        st.warning("Task cannot be empty!")

# Display tasks
st.subheader("Your TO-DO List")

if not st.session_state.tasks:
    st.info("No tasks added yet. Start by adding a task from the sidebar!")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])

        # Mark task as completed
        completed = col1.checkbox(f"**{task['task']}**", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed

        # Edit task
        if col2.button("Edit", key=f"edit_{index}"):
            new_task = st.text_input("Edit task", task["task"], key=f"edit_input_{index}")
            if new_task and st.button("Save", key=f"save_{index}"):
                st.session_state.tasks[index]["task"] = new_task
                st.experimental_rerun()

        # Delete task
        if col3.button("Delete", key=f"delete_{index}"):
            del st.session_state.tasks[index]
            st.experimental_rerun()

# Clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks.clear()
    st.success("All tasks deleted successfully!")

# Footer
st.markdown("---")
st.caption("Stay organized & productive with this simple TO-DO List App.")
