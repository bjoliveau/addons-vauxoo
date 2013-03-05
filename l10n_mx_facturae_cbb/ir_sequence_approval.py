# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2010 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: moylop260 (moylop260@vauxoo.com)
#    Launchpad Project Manager for Publication: Nhomar Hernandez - nhomar@vauxoo.com
############################################################################
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

from openerp.osv import fields, osv

class ir_sequence_approval(osv.osv):
    _inherit = 'ir.sequence.approval'

    def _get_type(self, cr, uid, context=None):
        types = super(ir_sequence_approval, self)._get_type(cr, uid, context=context)
        types.extend([
            ('cbb', 'CBB'),
        ])
        return types

    _columns = {
        'date_start': fields.date('Fecha de Aprobación', size=32,),
        'date_end': fields.date('Fecha de Vigencia', size=32,),
        'cbb_image': fields.binary('Imagen de Código de Barras Bidimensional'),
        'type': fields.selection(_get_type, 'Type', type='char', size=64, required=True, help="Type of Electronic Invoice"),
    }
ir_sequence_approval()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
