{
    'name': 'Course Enquiry Form',
    'version': '17.0.1.0.0',
    'category': 'CRM',
    'summary': 'Custom enquiry form that creates CRM leads',
    'description': 'An enquiry form that collects name, phone, email, and course interested, creating new opportunities.',
    'depends': ['crm','tijus_crm_custom'],
    'data': [
        'views/web_form.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
