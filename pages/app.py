from pages import root
from flask import render_template, request, redirect, url_for
from .excel.parse import sheet_data, set_sheet_values, STOCK_KEY


@root.route("/")
def index():
    return render_template("index.html")


@root.route("/store")
def store():

    return render_template("store.html", data=sheet_data)


@root.route("/order", methods=["POST"])
def order():
    res_all = request.form
    product_names = [product["商品名"] for product in sheet_data]
    for i, name in enumerate(product_names):
        bought_amount = res_all[name]
        sheet_data[i][STOCK_KEY] -= int(bought_amount)
        pass

    all_price = set_sheet_values(sheet_data)
    print(all_price)

    return redirect(url_for("store"))
