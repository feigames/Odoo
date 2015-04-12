# -*- coding: utf-8 -*-
import openerp.addons.decimal_precision as dp
from openerp import models,fields,api,exceptions, _
import time
import rongzi_paicheng


class rongzi_gouxiao(models.Model):

    _name='rongzi.gouxiao'

    _description=u'购销合同'

    name=fields.Char(u'编号',default=lambda self:self.env['ir.sequence'].get('rongzi.gouxiao') or '/',
    copy=False,readonly=True)

    state=fields.Selection([('draft',u'草稿'),('confirm',u'已审核')],u'状态',copy=False,readonly=True,
    track_visibility='onchange',default='draft')

    company_gf=fields.Many2one('res.company',u'供方',required=True,readonly=True,
    states={'draft':[('readonly',False)]},default=lambda self:self.env.user.company_id)

    company_xf=fields.Many2one('res.company',u'需方',required=True,readonly=True,
    states={'draft':[('readonly',False)]},default=lambda self:self.env.user.company_id)

    date=fields.Date(u'签订日期',default=fields.Date.today,required=True,copy=False,select=True,
    states={'draft':[('readonly',False)]},readonly=True)

    address=fields.Char(default=u"宁波",string=u'签订地点',required=True,select=True,
    states={'draft':[('readonly',False)]},readonly=True)

    amount=fields.Float(compute='_amount',string=u'总金额',method=True,select=True,store=True,
    readonly=True,digits_compute=dp.get_precision('Account'))

    line_ids=fields.One2many('rongzi.gouxiao.line','gouxiao_id',u'购销明细',copy=True,
    readonly=True,states={'draft':[('readonly',False)]})

    paicheng_id=fields.Many2one('rongzi.paicheng',u'排货路线',required=True,copy=True,
    readonly=True,states={'draft':[('readonly',False)]},domain=[('state','=','draft')])

    _sql_constraints = [
        ('code_gouxiao_uniq', 'unique (name)', u'购销编号号不允许重复!'),
    ]

    @api.one
    def action_view_confirm(self):
        self.state='confirm'

    @api.one
    def action_view_cancelled(self):
        self.state='draft'

    @api.one
    @api.depends('line_ids')
    def _amount(self):
        #total=0.0
        for line in self.line_ids:
            self.amount+=line.jine
        return self.amount

    @api.one
    @api.constrains('line_ids')
    def _check_line(self):
        if not self.line_ids:
            raise exceptions.ValidationError(_(u"必须要有货物明细!"))

    @api.one
    def unlink(self):
        if self.state != 'draft':
            raise exceptions.ValidationError(_(u'不能删除已经审核的记录!'))
        super(rongzi_gouxiao,self).unlink()

class rongzi_gouxiao_line(models.Model):

    _name='rongzi.gouxiao.line'

    _description=u'购销明细'

    gouxiao_id=fields.Many2one('rongzi.gouxiao','gouxiao_id',ondelete='cascade',select=True)

    product_id=fields.Many2one('product.product',u'产品',required=True,select=True)

    product_qty=fields.Float(u'数量',required=True)

    guige=fields.Char(u'规格型号')

    product_uom=fields.Many2one('product.uom', u'单位', required=True)

    jine=fields.Float(compute='_jine',string=u'金额',method=True,select=True,store=True,
    readonly=True,digits_compute=dp.get_precision('Account'))

    price=fields.Float(u'单价',select=True,digits_compute=dp.get_precision('Account'))

    @api.one
    @api.depends('price','product_qty')
    def _jine(self):
        self.jine=self.price*self.product_qty
        return self.jine

