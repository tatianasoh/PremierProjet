# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversitySubject(models.Model):
     _name = 'university.subject'
     name = fields.Char('name of subject')
     code = fields.Char('code of subject')