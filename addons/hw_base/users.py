# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _

class res_users(models.Model):
    _inherit = "res.users"
    department_id=fields.Many2one('hr.department','Department',required=True)
    job_id=fields.Many2one('hr.job','Job',required=True)


class hr_department(models.Model):
    _inherit = "hr.department"
    zhiguan=fields.Boolean(u'是否总经理直管')