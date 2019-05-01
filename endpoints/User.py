from app import app
# from controllers import User
from controllers import User

app.add_url_rule('/users/', view_func=User.get_all_users)
app.add_url_rule('/users/clear', view_func=User.clear_all_users, methods=['POST'])
app.add_url_rule('/users/add/', view_func=User.add_user, methods=['POST'])
