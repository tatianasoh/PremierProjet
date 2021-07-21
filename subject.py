# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversitySubject(models.Model):
     _name = 'university.subject'
     name = fields.Char('Name of Subject')
     code = fields.Char('Code of Subject')
     credit = fields.Integer('Nombre de credits')