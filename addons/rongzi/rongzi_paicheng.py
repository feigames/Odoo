# -*- coding: utf-8 -*-
import openerp.addons.decimal_precision as dp
from openerp import models,fields,api,exceptions, _


class rongzi_paicheng(models.Model):

    _name='rongzi.paicheng'

    _description=u'排货路线'

    name=fields.Char(u'内部编号',default=lambda self:self.env['ir.sequence'].get('rongzi.paicheng') or '/',
    copy=False,readonly=True)

    state=fields.Selection([('draft',u'草稿'),('confirm',u'归档')],u'状态',copy=False,readonly=True,
    track_visibility='onchange',default='draft')

    date_paicheng=fields.Date(u'日期',default=fields.Date.today,required=True,copy=False,select=True,
    states={'draft':[('readonly',False)]},readonly=True)


    amount=fields.Float(compute='_amount',string=u'总金额',method=True,select=True,store=True,
    readonly=True,digits_compute=dp.get_precision('Account'))


    xianlu=fields.Text(u'排货路线',states={'draft':[('readonly',False)]},readonly=True)


    line_ids=fields.One2many('rongzi.paicheng.line','paicheng_id',u'货物明细',copy=True,
    readonly=True,states={'draft':[('readonly',False)]})

    paicheng_gouxiao_count = fields.Integer(compute='_paicheng_gouxiao_count')

    _sql_constraints = [
        ('code_paicheng_uniq', 'unique (name)', u'排程号不允许重复!'),
    ]

    @api.one
    def _paicheng_gouxiao_count(self):
        count = self.env['rongzi.gouxiao'].search_count([('paicheng_id.name', '=', self.name)])
        self.paicheng_gouxiao_count = count

    @api.one
    @api.constrains('line_ids')
    def _check_line(self):
        if not self.line_ids:
            raise exceptions.ValidationError(_(u"必须要有货物明细!"))


    @api.one
    def unlink(self):
        if self.state != 'draft':
            raise exceptions.ValidationError(_(u'不能删除已经归档的记录!'))
        super(rongzi_paicheng,self).unlink()

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


class rongzi_paicheng_line(models.Model):

    _name='rongzi.paicheng.line'

    _description=u'货物明细'

    paicheng_id=fields.Many2one('rongzi.paicheng','paicheng_id',ondelete='cascade',select=True)

    product_id=fields.Many2one('product.product',u'产品',required=True,select=True)

    product_qty=fields.Float(u'数量',required=True)

    product_uom=fields.Many2one('product.uom', u'单位', required=True)

    jine=fields.Float(compute='_jine',string=u'金额',method=True,select=True,store=True,
    readonly=True,digits_compute=dp.get_precision('Account'))

    price=fields.Float(u'单价',select=True,digits_compute=dp.get_precision('Account'))


    @api.one
    @api.depends('price','product_qty')
    def _jine(self):
        self.jine=self.price*self.product_qty
        return self.jine

# class rongzi_paicheng_chupiao(models.Model):

#     _name='rongzi.paicheng.chupiao'

#     _description=u'出票明细'

#     chupiao_id=fields.Many2one('rongzi.paicheng','chupiao_id',ondelete='cascade',select=True)

#     yinhang_chupiao=fields.Many2one('rongzi.yinhang.line',u'出票银行',required=True)

#     company_chupiao=fields.Many2one('res.company',u'出票人',required=True)

#     company_shoupiao=fields.Many2one('res.company',u'收票人',reuqired=True)

#     date_jilu=fields.Date(u'登记日期',copy=False,readonly=True,default=fields.Date.today)

#     user_id=fields.Many2one('res.users',u'经办人',required=True,copy=False,
#     default=lambda self:self.env.user)

#     gaizhang=fields.Selection([('none',u'无'),('fp',u'发票联盖章'),('jz',u'记账联盖章'),('all',u'两联盖章')],u'盖章',default='none',required=True)

#     type_piaoju=fields.Selection([('gnz',u'国内证'),('yc',u'银承'),('dp',u'电票'),('other',u'其他')],u'票据类型',default='gnz',required=True)

#     date_kaishi=fields.Date(u'开始日期',copy=False,required=True,default=fields.Date.today)

#     date_jieshu=fields.Date(u'结束日期',copy=False,required=True,default=fields.Date.today)

#     jine=fields.Float(u'票面金额(万)',digits_compute=dp.get_precision('Account'))

#     bili=fields.Float(u'保证金(%)',digits_compute=dp.get_precision('Account'))

#     bzlv=fields.Float(u'保证金利率(%)',didgits_compute=dp.get_precision('Account'))

#     note=fields.Char(u'备注')



# class rongzi_paicheng_tiexian(models.Model):

#     _name='rongzi.paicheng.tiexian'

#     _description=u'贴现明细'

#     yinhang_chupiao=fields.Many2one('rongzi.yinhang.line',u'出票银行',required=True)

#     company_chupiao=fields.Many2one('res.company',u'出票人',required=True)

#     company_shoupiao=fields.Many2one('res.company',u'收票人',reuqired=True)

#     tiexian_id=fields.Many2one('rongzi.paicheng','tiexian_id',ondelete='cascade',select=True)

#     date=fields.Date(u'登记日期',copy=False,readonly=True,default=fields.Date.today)

#     user_id=fields.Many2one('res.users',u'经办人',required=True,copy=False,
#         default=lambda self:self.env.user)

#     luxian=fields.Text(u'背书路线')

#     company_tiexian=fields.Many2one('res.company',u'贴现人',reuqired=True)

#     yinhang_tiexian=fields.Many2one('rongzi.yinhang.line',u'贴现银行',required=True)

#     jine=fields.Float(u'金额(万)',digits_compute=dp.get_precision('Account'))

#     lilv=fields.Float(u'贴现利率(%)')

#     gaizhang=fields.Selection([('none',u'无'),('fp',u'发票联盖章'),('jz',u'记账联盖章'),('all',u'两联盖章')],u'盖章',default='none',required=True)

#     type_piaoju=fields.Selection([('gnz',u'国内证'),('yc',u'银承'),('dp',u'电票'),('other',u'其他')],u'票据类型',default='gnz',required=True)

#     note=fields.Char(u'备注')