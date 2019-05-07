from app import app
from controllers import Credentials


app.add_url_rule('/credentials/login/', view_func=Credentials.log_in, methods=["POST"])
app.add_url_rule('/credentials/signin/', view_func=Credentials.sign_in, methods=["POST"])
app.add_url_rule('/credentials/update/', view_func=Credentials.update_credentials, methods=["POST"])
app.add_url_rule('/credentials/delete/', view_func=Credentials.delete_credentials, methods=["POST"])
app.add_url_rule('/credentials/delete_all/', view_func=Credentials.delete_all_credentials, methods=["POST"])
