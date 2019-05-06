from app import app
from controllers import Task

app.add_url_rule('/status/', view_func=Task.get_all_tasks)
app.add_url_rule('/status/<name>', view_func=Task.get_get_one_tasks)
app.add_url_rule('/status/add/', view_func=Task.add_task, methods=['POST'])
app.add_url_rule('/status/update/', view_func=Task.upd_task, methods=['POST'])
app.add_url_rule('/status/delete/', view_func=Task.del_task)
app.add_url_rule('/status/clear/', view_func=Task.del_all_tasks, methods=['POST'])
