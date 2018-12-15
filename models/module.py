# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CodeGenerateModule(models.Model):
    _name = 'code.generate.module'

    sequence = fields.Integer(string='Module Sequence')
    name = fields.Char(string='Module Name')
    summary = fields.Char(string='Module Summary')
    description = fields.Char(string='Module Description')
    author = fields.Char(string='Author')
    website = fields.Char(string='Website')
    category = fields.Char(string='Category')
    version = fields.Char(string='Version')
    installable = fields.Char(string='Depends')
    application = fields.Char(string='Application')
    auto_install = fields.Char(string='Auto Install')
