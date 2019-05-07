from app import app
from controllers import User

app.add_url_rule('/users/', view_func=User.get_all_users)
app.add_url_rule('/users/<name>', view_func=User.get_one_user)
app.add_url_rule('/users/update/', view_func=User.upd_user, methods=['POST'])
app.add_url_rule('/users/clear/', view_func=User.del_all_users, methods=['POST'])
app.add_url_rule('/users/delete/', view_func=User.del_user)
