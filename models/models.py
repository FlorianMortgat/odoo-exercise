# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Exercise(models.Model):
    '''
    ORM model extending the SaleOrder ('sale.order') model provided by the
    'sale' module.
    '''
    _inherit = 'sale.order'

    # the 'name' field is already provided by the parent model

    # exercise field: a simple string field
    exercise = fields.Char(string="Exercise")

    # attempt at creating a non-stored computed field
    exercise_rot13 = fields.Char(string="Exercise rot13", compute="_rot13", store=False)


    @api.depends('exercise')
    def _rot13(self):
        """
        Computes the rot13 (toy cipher) ciphertext of
        the “exercise” field.
        """
        #self.value2 = float(self.value) / 100
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet += alphabet.lower()

        plain_text = self.exercise
        if not plain_text: 
            return
        ret = ""

        for char in plain_text:
            if char in alphabet:
                pos = alphabet.index(char)
                case_offset = 26 if pos >= 26 else 0

                char = alphabet[case_offset + (pos + 13) % 26]
            ret += char
        self.exercise_rot13 = ret
