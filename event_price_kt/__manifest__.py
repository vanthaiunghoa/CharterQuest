{
    "name": "Event Customization",
    "version": "11.2",
    "depends": ["base",
                "sale_management",
                "event_sale",
                "event",
                "event_price",
                "website_event",
                "website_sale",
                "stock",
        ],
    "sequence":1,
    "author": "Acespritech Solutions Pvt. Ltd.",
    "category": "Custom",
    "description": "Adds a custom Pricing to OpenERP events",
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'demo/paper_formate_data.xml',
        'views/pcexam_voucher_report.xml',
        'views/email_templates_data.xml',
        "views/event_view_inh_kt.xml",
        "views/report_view.xml",
        "views/customer_view.xml",
        "views/event_discount_view.xml",
        "views/semister_view.xml",
        'wizard/pcexam_wizard_view.xml',
        'report/sale_pcexam_report.xml',
        'report/sale_enrollment_report.xml',
        'report/sale_charterbook_report.xml',
        'report/invoice_pcexam_report.xml',
        'report/invoice_enrollment_report.xml',
        'report/invoice_charterbook_report.xml',
        'report/statement_enrollment_report.xml',
    ],
    'css': ['static/src/css/my_style.css'],
    "installable": True,
    "active": False
}
