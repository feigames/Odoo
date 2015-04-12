# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2009 Gábor Dukai
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': '台灣會計科目表 - Accounting',
    'version': '1.0',
    'category': 'Localization/Account Charts',
    'author': '',
    'maintainer':'',
    'website':'',    
    'description': """
添加科目類型\會計科目表模板
============================================================
    """,
    'depends': ['base','account'],
    'demo': [],
    'data': [
        'account_chart.xml',
        'l10n_chart_tw_wizard.xml',        
    ],
    'license': 'GPL-3',
    'auto_install': False,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

