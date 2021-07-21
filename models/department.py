# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityDepartment(models.Model):
     _name = 'university.department'
     name = fields.Char('name of department')
     code = fields.Char('code of department')