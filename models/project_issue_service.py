# -*- coding: utf-8 -*-
##############################################################################
#
#    Michael Watchorn
#    Copyright (C) 2016 (www.TheWatchornGroup.com)
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

from openerp import fields, models, api

class project_issue_service(models.Model):
    """Service and Warranty work done for Projects, meant for after the project has been deployed."""
    _inherit = "project.issue"

    #Issue Service Basics
    ###name = fields.Char("Summary")
    ###project_id = fields.Many2one("project.name", string='Project')
    ###description = fields.Char("Description of Issue")
    resolution = fields.Char("Resolution to Issue")
    warranty_call = fields.Boolean("Warranty Call")
    service_call = fields.Boolean("Service Call")
    follow_up = fields.Boolean("Follow Up")
    service_personnel_ids = fields.Many2many(comodel_name="res.user", string="Service Personnel")
    start_delay = fields.Integer("Days to service (Days)")
    ###duration = fields.Integer("Work Duration (Days)")

    #Costs
    total_cost = fields.Float("Total Service Cost")
    cust_amount = fields.Float("Customer Amount")
    loss_amount = fields.Float("Loss Amount (Not charged to customer)")
    invoice = fields.Char("Invoice Number")

    #Project Contact Information
    contact_info = fields.Many2one(string="(Project) Contact Information")

    #Dates:
    request_date = fields.Date("Request Date")
    work_start_date = fields.Date("Service Start Date")
    work_complete_date = fields.Date("Service Complete Date")


class user_service_personnel(models.Model):
    """ Add the 'service person' option to users, so they can be easily flagged and filtered to only who the list of selected people."""
    _inherit = "res.users"

    is_service_personnel = fields.Boolean("Service Personnel", help="This person may go on-site for service calls.")

class project_contact_info(models.Model):
    """This is the contact information for a particular company location."""
    _name = "project.contact_info"

    name = fields.Char()
    customer = fields.Many2one(comodel_name="res.partner", help="The customer to whom the project was sold", delegate=True)
    customer_location = fields.Char(default='_Loc_City_State_Country')
    primary_contact_id = fields.Many2one(comodel_name="res.users", string="Primary Contact", domain="[('is_service_personnel','=',True)]")
    secondary_contact_id = fields.Many2one(comodel_name="res.user", string="Secondary Contact", domain="[('is_service_personnel','=',True)]")
    project_ids  = fields.Many2many(comodel_name='project.project', inverse_name='project_id', string='Projects associated with these contacts')

    @api.one
    @api.depends('customer')
    def _Loc_City_State_Country(self):
        if len(customer.city)>0:
            location = customer.city + ', '
        if len(customer.state)>0:
            location = location + customer.state +  ', '
        if len(customer.country)>0:
            location = location + customer.country + ', ' #extra comma and space added so the return value is consistently all but the last 2 characters.
        return location[:-2]
