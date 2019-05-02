from app import app
from controllers import Category

app.add_url_rule('/categories/', view_func=Category.get_all_categories)
app.add_url_rule('/category/<name>', view_func=Category.get_one_category)
app.add_url_rule('/categories/add/', view_func=Category.add_category, methods=['POST'])
app.add_url_rule('/categories/update/', view_func=Category.upd_category, methods=['POST'])
app.add_url_rule('/categories/delete/', view_func=Category.del_category)
app.add_url_rule('/categories/clear/', view_func=Category.del_all_categories, methods=['POST'])
