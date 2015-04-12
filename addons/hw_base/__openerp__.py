# -*- encoding: utf-8 -*-
# __author__ = feigames@qq.com
##############################################################################
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

{
    'name' : '海外费用报销基础',  #模块名称
    'version' : '8.0',    
    'description' : '''   
    海外费用报销基础模块
    增加：
        用户界面增加部门
    ''',
    'author' : '徐勇',
    'website' : 'feigames@qq.com',
    'depends' : ['base','hr','multi_company'],
    'data' : [          #此处的xml文件如果menu跟action还有form等分开放，需要注意先后顺序
                'views/res_users_view.xml',
                'views/hr_department_view.xml',
    ],
    'installable' : True,
    'certificate' : '',
    'category' : '',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: