# sid_sale_line_core

## PropÃ³sito
MÃ³dulo funcional que agrupa los **campos core** y **cÃ³mputos auxiliares** sobre `sale.order.line`.

Incluye:
- `contractual_qty`
- `sid_has_po_delay` (flag sincronizado desde compra)
- `familia` (related a la categorÃ­a del producto)
- `pending_invoice`, `pending_delivery` (compute/store)

## Dependencias
- `sale`, `sale_stock`, `stock`
- `oct_fecha_contrato_ventas`

## RelaciÃ³n con otros mÃ³dulos
- `sid_sale_line_stock`: aÃ±ade stock pronosticado por almacÃ©n.
- `sid_sale_line_custom_fields`: mÃ³dulo paraguas/meta para compatibilidad de dependencias.
