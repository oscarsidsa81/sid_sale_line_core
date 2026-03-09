# sid_sale_line_core

## Propósito
Módulo funcional que agrupa los **campos core** y **cómputos auxiliares** sobre `sale.order.line`.

Incluye:

- `contractual_qty`
- `sid_has_po_delay` (flag sincronizado desde compra)
- `familia` (related a la categoría del producto)
- `pending_invoice`, `pending_delivery` (compute/store)

## Campos incluidos

### Cantidades contractuales
- `contractual_qty`  
Cantidad contractual asociada a la línea de venta.

### Sincronización con compras
- `sid_has_po_delay`  
Flag booleano sincronizado desde compras que indica si la línea de venta tiene **retraso en alguna línea de compra vinculada**.

### Información del producto
- `familia`  
Campo `related` a la **categoría del producto**.

### Estados pendientes
Campos calculados y almacenados (`compute`, `store=True`) para permitir filtros, agrupaciones y análisis.

- `pending_invoice`  
Importe o cantidad pendiente de facturar.

- `pending_delivery`  
Cantidad pendiente de entregar.

## Dependencias

- `sale`
- `sale_stock`
- `stock`
- `oct_fecha_contrato_ventas`

## Relación con otros módulos

### `sid_sale_line_stock`
Añade información de **stock pronosticado por almacén**.

### `sid_sale_line_custom_fields`
Módulo **paraguas/meta** utilizado para compatibilidad de dependencias.