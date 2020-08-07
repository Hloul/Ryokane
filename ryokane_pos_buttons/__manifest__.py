{
    "name": "Ryokane POS Buttons",
    "version": "12.0.1.3.1",
    "category": "Point of Sale",
    "author": "Babatope Ajepe",
    "website": "https://ajepe.github.io",
    "license": "LGPL-3",
    "depends": ["point_of_sale", "hr", "stock", "sale_stock", "partner_category_hierarchy"],
    "data": ["security/ir.model.access.csv","views/assets.xml", "views/pos_order.xml",],
    "qweb": ["static/src/xml/pos.xml"],
    "application": False,
    "installable": True,
}
