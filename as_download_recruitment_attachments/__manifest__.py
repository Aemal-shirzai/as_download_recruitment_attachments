# -*- coding: utf-8 -*-
{
    'name': "Download Batch Recruitment Attachments",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Aemal Shirzai",
    'website': "https://aemal-shirzai.github.io/portfolio/",
    'category': 'Human Resources/Recruitment',
    'version': '0.1',
    'depends': ['base', 'hr_recruitment'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/download_wizard.xml',
        'views/hr_job.xml'
    ],
}
