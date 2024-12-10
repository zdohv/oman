import json

TODO_FILE = 'todos.json'

def load_todo():
    try:
        with open(TODO_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return {}
    
def save_todo(data):
    with open(TODO_FILE, 'w', endcoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_todo(user_id, descripprion, due_data):
    data = load_todo()
    user_tasks = data.get(str(user_id), [])
    task_id = len(user_tasks) + 1
    task = {'id': task_id, 'description': descripprion,'due_data':due_data}
    user_tasks.append(task)
    data[str(user_id)] = user_tasks
    save_todo(data)