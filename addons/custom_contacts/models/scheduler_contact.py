
from odoo import models
from datetime import datetime

class scheduler_contact(models.Model):
    _inherit = 'res.partner'

    def action_add_comment(self):
        now = datetime.now()
        # contacts = self.env['res.partner'].search([['comment', 'not ilike', 'Updated on']], limit=2)
        contacts = self.env['res.partner'].search([['comment','=',False]], order='name desc', limit=2)
        # print(contacts)

        if(len(contacts)):
            for contact in contacts:
                date_now = 'Updated on ' + now.strftime("%d/%m/%Y %H:%M:%S")
                contact.comment = date_now
                print(contact.id)
                print(contact.comment)
