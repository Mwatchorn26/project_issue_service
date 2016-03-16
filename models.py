# -*- coding: utf-8 -*-

from openerp import models, fields, api


class project_issue_service(models.Model):
    """Service and Warranty work done for Projects, meant for after the project has been deployed."""
    _inherit = "project.issue"

    #Issue Service Basics
    ###name = fields.Char("Summary")
    ###project_id = fields.Many2one("project.name", string='Project')
    ###description = fields.Char("Description of Issue")
    resolution = fields.Text(string="Resolution to Issue", required=False)
    #warranty_call = fields.Boolean(string="Warranty Call", default=False)
    #service_call = fields.Boolean("Service Call")
    #follow_up = fields.Boolean("Follow Up")
    start_delay = fields.Integer("Days to service (Days)")
    ###duration = fields.Integer("Work Duration (Days)")

    #Costs
    total_cost = fields.Float("Total Service Cost")
    cust_amount = fields.Float("Customer Amount")
    loss_amount = fields.Float("Loss Amount (Not charged to customer)")
    invoice = fields.Char("Invoice Number")

    site_contact_ids = fields.Many2many(related='project_id.site_contact_ids', string='Site Contacts')

#    #Project Contact Information
#    #contact_info = fields.Many2one(comodel_name="project.contact_info", string="(Project) Contact Information")

    #Dates:
    request_date = fields.Date("Request Date")
    work_start_date = fields.Date("Service Start Date")
    work_complete_date = fields.Date("Service Complete Date")

    service_personnel_ids = fields.Many2many(comodel_name="hr.employee", string="Service Team", domain="[('is_service_personnel','=',True)]", help="These are your company employees who go out to customer sites to perform service functions.")

class hr_employee(models.Model):
    """ Add the 'service person' option to employees, so they can be easily flagged and filtered."""
    _inherit = "hr.employee"

    is_service_personnel = fields.Boolean("Service Personnel", help="This person may go on-site for service calls.")


class res_partner(models.Model):
    """ Add the 'service person' option to users, so they can be easily flagged and filtered."""
    _inherit = "res.partner"

    project_ids = fields.Many2many("project.project", string="Projects", help="These are the projects associated with this partner.")


class project(models.Model):
    """Inherit the project, and adds the contacts for both sides."""
    _inherit = "project.project"

    #location = fields.Char(default='_Loc_City_State_Country')
    #site_contact_ids = fields.One2many("res.partner", 'project_ids', string="Site Contacts", help="These are your counterparts, the people you contact who work for the customer company.")

#domain="[('is_company','=',False)]",

    site_contact_ids = fields.Many2many("res.partner", string="Site Contacts", domain="[('is_company','=',False)]",
help="These are your counterparts, the people you contact who work for the customer company.")

#['&', (res.partners,'not in',res.users.ids),



