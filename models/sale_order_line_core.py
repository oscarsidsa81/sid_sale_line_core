from odoo import api, fields, models
from odoo.tools.float_utils import float_compare


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    contractual_qty = fields.Float(string="Cantidad contractual")

    sid_has_po_delay = fields.Boolean(
        string="Retraso en compra",
        store=True,
        index=True,
        readonly=False,
        # si quieres permitir override manual, si no: readonly=True
    )

    familia = fields.Char(
        string="Familia",
        related="product_id.categ_id.name",
        store=True,
        readonly=True,
    )

    pending_invoice = fields.Selection(
        [
            ("to_invoice", "A facturar"),
            ("invoiced", "Facturado"),
            ("no", "N/A"),
        ],
        string="Pendiente FacturaciÃ³n",
        compute="_compute_pending_invoice",
        store=True,
        readonly=True,
    )

    pending_delivery = fields.Selection(
        [
            ("pending", "Pendiente"),
            ("ok", "OK"),
        ],
        string="Pendiente Entrega",
        compute="_compute_pending_delivery",
        store=True,
        readonly=True,
    )

    @api.depends("qty_to_invoice", "qty_invoiced", "state")
    def _compute_pending_invoice(self):
        for line in self:
            if line.state == "cancel":
                line.pending_invoice = "no"
                continue
            if float_compare(line.qty_to_invoice or 0.0, 0.0, precision_digits=2) > 0:
                line.pending_invoice = "to_invoice"
            elif float_compare(line.qty_invoiced or 0.0, 0.0, precision_digits=2) > 0:
                line.pending_invoice = "invoiced"
            else:
                line.pending_invoice = "no"

    @api.depends("qty_delivered", "product_uom_qty", "state")
    def _compute_pending_delivery(self):
        for line in self:
            if line.state == "cancel":
                line.pending_delivery = "ok"
                continue
            remaining = (line.product_uom_qty or 0.0) - (line.qty_delivered or 0.0)
            line.pending_delivery = "pending" if float_compare(remaining, 0.0, precision_digits=2) > 0 else "ok"
