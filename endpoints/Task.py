from app import app
from controllers import Task

app.add_url_rule('/task/', view_func=Task.get_all_tasks)
app.add_url_rule('/task/<name>', view_func=Task.get_get_one_tasks)
app.add_url_rule('/task/add/', view_func=Task.add_task, methods=['POST'])
app.add_url_rule('/task/update/', view_func=Task.upd_task, methods=['POST'])
app.add_url_rule('/task/delete/', view_func=Task.del_task)
app.add_url_rule('/task/clear/', view_func=Task.del_all_tasks, methods=['POST'])
