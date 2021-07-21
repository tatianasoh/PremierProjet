# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityStudent(models.Model):
     _name = 'university.student'
     f_name = fields.Char('first name')
     l_name = fields.Char('last name')
     sex = fields.Selection([('male','Male'),('female','Female')])
     identityCard = fields.Char('Identity card')
     address = fields.Text('address')
     birthday = fields.Date('birthday')
     registrationDate = fields.DateTime('registration date')
     email = fields.Char()
     phone = fields.Char()

