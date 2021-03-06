# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp import http
from openerp.http import request
from openerp import SUPERUSER_ID
from datetime import datetime
import werkzeug
import pytz
import re

import logging
_logger = logging.getLogger(__name__)


class crm_lead(models.Model):
    _inherit = 'crm.lead'

    @api.one
    def _mass_mail_count(self):
        self.mass_mail_count = len(self.env['mail.mail.statistics'].select(['&',('res_id','=',self.id),('model','=','crm.lead')]))

    mass_mail_count = fields.Float('Mass Mail Count',compute=lambda self: len(self.env['mail.mail.statistics'].select(['&',('res_id','=',self.id),('model','=','crm.lead')]))
