# -*- coding: utf-8 -*-
from odoo import http

# class Code-generation(http.Controller):
#     @http.route('/code-generation/code-generation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/code-generation/code-generation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('code-generation.listing', {
#             'root': '/code-generation/code-generation',
#             'objects': http.request.env['code-generation.code-generation'].search([]),
#         })

#     @http.route('/code-generation/code-generation/objects/<model("code-generation.code-generation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('code-generation.object', {
#             'object': obj
#         })