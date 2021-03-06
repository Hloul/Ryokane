# coding: utf-8
#
# Copyright © Lyra Network.
# This file is part of Sogecommerce plugin for Odoo. See COPYING.md for license details.
#
# Author:    Lyra Network (https://www.lyra.com)
# Copyright: Copyright © Lyra Network
# License:   http://www.gnu.org/licenses/agpl.html GNU Affero General Public License (AGPL v3)

from odoo import _

# WARN: Do not modify code format here. This is managed by build files.
SOGECOMMERCE_PLUGIN_FEATURES = {
    'multi': True,
    'restrictmulti': True,
    'qualif': False,
    'shatwo': True,
}

SOGECOMMERCE_PARAMS = {
    'GATEWAY_CODE': 'Sogecommerce',
    'GATEWAY_NAME': 'Sogecommerce',
    'BACKOFFICE_NAME': 'Sogecommerce',
    'SUPPORT_EMAIL': 'support@sogecommerce.societegenerale.eu',
    'GATEWAY_URL': 'https://sogecommerce.societegenerale.eu/vads-payment/',
    'SITE_ID': '12345678',
    'KEY_TEST': '1111111111111111',
    'KEY_PROD': '2222222222222222',
    'CTX_MODE': 'TEST',
    'SIGN_ALGO': 'SHA-256',
    'LANGUAGE': 'fr',

    'GATEWAY_VERSION': 'V2',
    'PLUGIN_VERSION': '1.2.1',
    'CMS_IDENTIFIER': 'Odoo_10-14',
}

SOGECOMMERCE_LANGUAGES = {
    'cn': 'Chinese',
    'de': 'German',
    'es': 'Spanish',
    'en': 'English',
    'fr': 'French',
    'it': 'Italian',
    'jp': 'Japanese',
    'nl': 'Dutch',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'sv': 'Swedish',
    'tr': 'Turkish',
}

SOGECOMMERCE_CARDS = {
    'CB': u'CB',
    'E-CARTEBLEUE': u'e-Carte Bleue',
    'MAESTRO': u'Maestro',
    'MASTERCARD': u'Mastercard',
    'VISA': u'Visa',
    'VISA_ELECTRON': u'Visa Electron',
    'VPAY': u'V PAY',
    'AMEX': u'American Express',
    'APETIZ': u'Apetiz',
    'AURORE-MULTI': u'Cpay Aurore',
    'CHQ_DEJ': u'Chèque Déjeuner',
    'CONECS': u'Conecs',
    'CVCO': u'Chèque-Vacances Connect',
    'EDENRED': u'Ticket Restaurant',
    'EDENRED_EC': u'Ticket EcoCheque',
    'EDENRED_TR': u'Ticket Restaurant',
    'E_CV': u'e-Chèque-Vacances',
    'FRANFINANCE_3X': u'Paiement en 3 fois',
    'FRANFINANCE_4X': u'Paiement en 4 fois',
    'FULLCB3X': u'Paiement en 3 fois CB',
    'ILLICADO': u'Carte Illicado',
    'ILLICADO_SB': u'Carte Illicado (sandbox)',
    'JCB': u'JCB',
    'ONEY_3X_4X': u'Paiement en 3 ou 4 fois Oney',
    'ONEY_ENSEIGNE': u'Cartes enseignes Oney',
    'PAYLIB': u'Paylib',
    'PAYPAL': u'PayPal',
    'PAYPAL_SB': u'PayPal Sandbox',
    'PICWIC': u'Carte Picwic',
    'PICWIC_SB': u'Carte Picwic (sandbox)',
    'SDD': u'Prélèvement SEPA',
    'SODEXO': u'Pass Restaurant',
}

SOGECOMMERCE_CURRENCIES = [
    ['AUD', '036', 2],
    ['KHR', '116', 0],
    ['CAD', '124', 2],
    ['CNY', '156', 1],
    ['CZK', '203', 2],
    ['DKK', '208', 2],
    ['HKD', '344', 2],
    ['HUF', '348', 2],
    ['INR', '356', 2],
    ['IDR', '360', 2],
    ['JPY', '392', 0],
    ['KRW', '410', 0],
    ['KWD', '414', 3],
    ['MYR', '458', 2],
    ['MXN', '484', 2],
    ['MAD', '504', 2],
    ['NZD', '554', 2],
    ['NOK', '578', 2],
    ['PHP', '608', 2],
    ['RUB', '643', 2],
    ['SGD', '702', 2],
    ['ZAR', '710', 2],
    ['SEK', '752', 2],
    ['CHF', '756', 2],
    ['THB', '764', 2],
    ['TND', '788', 3],
    ['GBP', '826', 2],
    ['USD', '840', 2],
    ['TWD', '901', 2],
    ['TRY', '949', 2],
    ['EUR', '978', 2],
    ['PLN', '985', 2],
    ['BRL', '986', 2],
]
