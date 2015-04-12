# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
import time
import datetime
class qingjia_qingjd(osv.Model):
    _name='qingjia.qingjd'
    _description=u'请假单'

    def _zje_all(self, cr, uid, ids, field_name, arg, context=None):
        res={}
        for contract in self.browse(cr, uid, ids, context=context):
            zje = 0
            for cost in contract.qjd_mx:
                zje += cost.jine
            res[contract.id] = zje
        return res

    def on_change_mx_jine(self, cr, uid, ids, qjd_mx, context=None):
        for contract in self.browse(cr, uid, ids, context=context):
         totalsum = 0.0
        for cost in contract.qjd_mx:
         totalsum += cost.jine
         return {
            'value': {
             'zje': totalsum,
            }
       }

    _columns={
          'tians':fields.float(u'请假天数',required=True),
          'kaisrq':fields.date(u'开始日期',required=True),
          'shiyou': fields.text(u'请假事由'),
          'qjd_mx': fields.one2many('qjd.mx', 'qjd_id', u'明细测试', copy=True),
          'zje': fields.function(_zje_all,string=u'合计测试',method=True,type='float'),
             }


class qjd_mx(osv.Model):
    _name='qjd.mx'
    _description=u'请假单明细'

    _columns={
          'jine':fields.float(u'金额'),
          'note': fields.text(u'备注'),
          'qjd_id': fields.many2one('qingjia.qingjd', required=True, ondelete='cascade', select=True, ),
             }