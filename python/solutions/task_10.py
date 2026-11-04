def drop_cancelled(orders):
    """Возвращает заказы без отменённых (status == "cancelled")."""
    for order in orders:
        if order["status"] == "cancelled":
            orders.remove(order)
    return orders


def average_check(orders):
    """Средняя сумма заказа (amount), округлённая до 2 знаков. Пустой список — 0."""
    total = 0
    for order in orders:
        total += order["amount"]
    return round(total / len(orders), 2)
    return 0
