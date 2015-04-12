# -*- coding: utf-8 -*-
import openerp.addons.decimal_precision as dp
from openerp import models,fields,api,exceptions, _


class rongzi_yinhang(models.Model):
    _name='rongzi.yinhang'

    _description=u'总行'

    name=fields.Char(u'总行',required=True)

    _sql_constraints = [
        ('code_zonghang_uniq', 'unique (name)', u'总行名称不允许重复!'),
    ]

   


class rongzi_yinhang_line(models.Model):
    _name='rongzi.yinhang.line'

    _description=u'分行'

    name=fields.Char(u'分行名称',required=True)

    zonghang_id=fields.Many2one("rongzi.yinhang",u'所属总行',required=True)

    _sql_constraints = [
        ('code_fenhang_uniq', 'unique (name)', u'分行名称不允许重复!'),
    ]