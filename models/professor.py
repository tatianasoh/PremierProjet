# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityProfessor(models.Model):
    _name = 'university.professor'
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    sex = fields.Selection([('male', 'Male'), ('female', 'Female')])
    identityCard = fields.Char('Identity card')
    address = fields.Text('address')
    birthday = fields.Date('birthday')
    startDate = fields.DateTime('date of starting')
    email = fields.Char()
    phone = fields.Char()