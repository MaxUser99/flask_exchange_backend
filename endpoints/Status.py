from app import app
from controllers import Status

app.add_url_rule('/status/', view_func=Status.get_all_statuses)
app.add_url_rule('/status/<name>', view_func=Status.get_one_status)
app.add_url_rule('/status/add/', view_func=Status.add_status, methods=['POST'])
app.add_url_rule('/status/update/', view_func=Status.upd_status, methods=['POST'])
app.add_url_rule('/status/delete/', view_func=Status.del_status)
app.add_url_rule('/status/clear/', view_func=Status.del_all_statuses, methods=['POST'])
