# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'CR Import Vendor Bills',
    'version': '12.0.1.0.1',
    'category': 'Vendor Bills',
    'author': 'CR FACTURA',
    'license': 'AGPL-3',
    'website': 'http://www.crfactura.com/',
    'summary': 'Import Vendor Bills from incoming mail server',

    'description': """
        
    """,

    # any module necessary for this one to work correctly
    'depends': ['fecr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_company_views.xml',
        'views/account_view.xml',
        'views/account_invoice_view.xml',
        'wizard/cr_multiple_invoice_validation_wz_view.xml',
    ]
    ,
}