##############################################################################
#
#   OpenERP, Open Source Management Solution
##############################################################################

{
    'name': 'devithesk',
    'version': '16.0.0.0.1',
    'author': 'Pablo holguin',
    'maintainer': 'Pablo holguin',
    'website': 'http://www.ithesk.com',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Short summary.',
    'depends': ['base','repair'],
    'data': [
      'views/repair_views.xml',
      'report/repair_reports2.xml',
      'report/repair_templates_repair_order2.xml',     
    ],
    'images': ['static/description/icon.png'],
    'images': ['static/img/logolabel.png'],
}
