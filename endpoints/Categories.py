from app import app
from controllers import Categories

app.add_url_rule('/categories/', view_func=Categories.get_all_categories)
app.add_url_rule('/categories/clear', view_func=Categories.clear_all_categories, methods=['POST'])
app.add_url_rule('/categories/add/', view_func=Categories.add_category, methods=['POST'])
