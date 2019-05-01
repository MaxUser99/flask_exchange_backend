from app import app
from controllers import User

app.add_url_rule('/users/', view_func=User.all_users, methods=['GET'])
app.add_url_rule('/users/add/', view_func=User.add_user, methods=['POST'])
