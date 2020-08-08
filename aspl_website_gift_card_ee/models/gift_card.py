# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
from odoo import models, fields, api
import time, datetime
import base64
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode


class WebsiteGiftCard(models.Model):
    # _name = "website.gift.card"
    _inherit = 'aspl.gift.card'
    _rec_name = "card_no"

    def random_cardno(self):
        return int(time.time())

    # card_no = fields.Char(string="Card No", default=random_cardno, readonly=True)
    # card_value = fields.Float(string="Card Value")
    # customer_id = fields.Many2one('res.partner', string="Customer")
    # issue_date = fields.Date(string="Issue Date", default=datetime.datetime.now().date())
    # expire_date = fields.Date(string="Expire Date")
    # pin_no = fields.Integer(string="Pin No.")
    # is_active = fields.Boolean('Active', default=True)
    # used_line = fields.One2many('gift.card.use', 'card_id', string="Used Line", oncascade='delete')
    # recharge_line = fields.One2many('gift.card.recharge', 'card_id', string="Recharge Line", oncascade='delete')
    encrypted_id = fields.Char(string='Encrypted Id')
    receiver_msg = fields.Char(string="Receiver Message")

    @api.model
    def create(self, vals):
        res = super(WebsiteGiftCard, self).create(vals)
        MASTER_KEY = "Some-long-base-key-to-use-as-encyrption-key"
        message = str(res['id'])
        cipher = encrypt(MASTER_KEY, message)
        encoded_cipher = b64encode(cipher)
        res['encrypted_id'] = encoded_cipher
        template_id = self.env['ir.model.data'].get_object_reference('aspl_website_gift_card_ee',
                                                                     'email_template__buy_card')
        if template_id and template_id[1]:
            template_obj = self.env['mail.template'].browse(template_id[1])
            template_obj.send_mail(res.id, force_send=True)

        return res


class GiftCardUse(models.Model):
    _inherit = 'aspl.gift.card.use'
    order_id = fields.Many2one("sale.order", string="Order")


class GiftCardRecharge(models.Model):
    _inherit = 'aspl.gift.card.recharge'

    @api.model
    def create(self, vals):
        res = super(GiftCardRecharge, self).create(vals)
        template_id = self.env['ir.model.data'].get_object_reference('aspl_website_gift_card_ee',
                                                                     'email_template_recharge_card')
        if template_id and template_id[1]:
            template_obj = self.env['mail.template'].browse(template_id[1])
            template_obj.send_mail(res.id, force_send=True)

        return res


class Product(models.Model):
    _inherit = 'product.product'

    is_gift_card = fields.Boolean(string="is gift card")


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    gift_card_value = fields.Float(string="Gift Card Amount")
    card_type = fields.Many2one('aspl.gift.card.type', string="Card Type")
    gift_card_id = fields.Many2one('aspl.gift.card', string="Gift Card")
    gift_card_use_ids = fields.One2many('aspl.gift.card.use', 'order_id', string="Gift Card Use")
    receiver_email = fields.Char(string="Receiver Email")
    receiver_name = fields.Char(string="Receiver Name")
    receiver_msg = fields.Char(string="Personal Message")

    @api.multi
    def write(self, vals):
        for so in self:
            if vals.get('state') == 'sale' or vals.get('state') == 'done':
                sale_order_line_id = self.env['sale.order.line'].sudo(1).search([('order_id', '=', so.id),
                                                                         ('product_id.is_gift_card', '=', True)])
                if sale_order_line_id:
                    if not so.gift_card_id:
                        qty = sale_order_line_id.product_uom_qty
                        gift_card_value = sale_order_line_id.price_subtotal / qty
                        while qty > 0:
                            gift_card_obj = self.env['aspl.gift.card']
                            gift_card_obj.create({
                                'card_value': gift_card_value,
                                'customer_id': self.partner_id.id,
                                'email': so.receiver_email,
                                'user_name': so.receiver_name,
                                "card_type": self.card_type.id,
                                "receiver_msg": self.receiver_msg,
                            })
                            qty -= 1
                            time.sleep(2)
                    if so.gift_card_id:
                        gift_card_obj = self.env['aspl.gift.card'].search([('id', '=', so.gift_card_id.id)])
                        if gift_card_obj:
                            gift_card_obj.write({
                                'card_value': gift_card_obj.card_value + sale_order_line_id.price_subtotal,
                            })
                        self.env['gift.card.recharge'].create({
                            'card_id': so.gift_card_id.id,
                            'amount': sale_order_line_id.price_subtotal,
                            "card_type": self.card_type.id,
                        })
            res = super(SaleOrder, self).write(vals)
            return res


class GiftCardValue(models.Model):
    _name = 'gift.card.value'

    active = fields.Boolean(string="Active", default=True)
    amount = fields.Float(string="Amount")
    sequence = fields.Integer(string="Sequence")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
