# -*- encoding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    event = fields.Many2one(comodel_name='event.event', string="Event")