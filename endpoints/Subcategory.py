from app import app
from controllers import Subcategory

app.add_url_rule('/subcategories/', view_func=Subcategory.get_all_subcat)
app.add_url_rule('/subcategories/<name>', view_func=Subcategory.get_one_subcat)
app.add_url_rule('/subcategories/add/', view_func=Subcategory.add_subcat, methods=['POST'])
app.add_url_rule('/subcategories/update/', view_func=Subcategory.upd_subcat, methods=['POST'])
app.add_url_rule('/subcategories/delete/', view_func=Subcategory.del_subcat)
app.add_url_rule('/subcategories/clear/', view_func=Subcategory.del_all_subcat, methods=['POST'])
