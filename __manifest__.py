# -*- coding: utf-8 -*-
{
    "name": "sid_sale_line_core",
    "version": "15.0.1.0.0",
    "category": "Sales",
    "summary": "Campos core y estados auxiliares en sale.order.line.",
    "author": "oscarsidsa81",
    "license": "LGPL-3",
    "depends": ["sale", "sale_stock", "stock", "oct_fecha_contrato_ventas","oct_product_extra_fields"],
    "data": [
        "views/sale_order_line_core_search.xml",
    ],
    "installable": True,
    "application": False,
}
