# -*- coding: utf-8 -*-
{
    'name': "Download Batch Recruitment Attachments",

    'summary': """"Download batch recruitment attachments for specific announcement""",

    'description': """
This application is a tool that simplifies the process of downloading all attachments submitted by applicants 
for a specific job announcement. It allows the user to select the job announcement and quickly download all the 
attachments as a single zip file. This feature can save time and effort for recruiters or hiring managers who need to review a 
large number of applications with multiple attachments. The user-friendly interface and simple navigation make it easy to use, 
and the zip file format ensures that all attachments are organized and easily accessible.
    """,

    'author': "Aemal Shirzai",
    'website': "https://aemal-shirzai.github.io/portfolio",
    'support': 'aemalshirzai2016@gmail.com',
    'price': '0',
    'currency': 'USD',
    'application': True,
    'version': '15.0.0.1.0.0',
    "license": "OPL-1",
    'category': 'Human Resources/Recruitment',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'hr_recruitment'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/download_wizard.xml',
        'views/hr_job.xml'
    ],
}
