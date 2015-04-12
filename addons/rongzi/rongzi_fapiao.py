# -*- coding: utf-8 -*-
import openerp.addons.decimal_precision as dp
from openerp import models,fields,api,exceptions, _


class rongzi_fapiao(models.Model):
    _name='rongzi.fapiao'

    _description=u'发票'

    name=fields.Char(u'发票号',required=True,copy=False)

    jine=fields.Float(u'发票金额(万元)',digits_compute=dp.get_precision('Account'))

    image_jz=fields.Binary(u'记账联',copy=False)

    image_fp=fields.Binary(u'发票联',copy=False)

    image_dk=fields.Binary(u'抵扣联',copy=False)

    _sql_constraints = [
        ('code_fapiao_uniq', 'unique (name)', u'发票号不允许重复!'),
    ]