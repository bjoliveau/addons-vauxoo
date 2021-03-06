# -*- encoding: utf-8 -*-
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#    coded by: hugo@vauxoo.com
#    planned by: Nhomar Hernandez <nhomar@vauxoo.com>
############################################################################

{
    "name": "Sale Order Create Task with Planned Hours",
    "summary": "Create the task with planned hours calculated in the SO",
    "version": "1.5",
    "author": "Vauxoo",
    "website": "http://www.vauxoo.com/",
    "category": "sale",
    "depends": [
        "sale_service",
    ],
    "data": [
        "view/sale_order_view.xml",
    ],
    "demo": [],
    "test": [],
    "qweb": [],
    "js": [],
    "css": [],
    "installable": True,
}
