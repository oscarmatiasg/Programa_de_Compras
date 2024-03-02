from ownable import Ownable

class Cart(Ownable):
    from item_manager import show_items

    def __init__(self, owner):
        super().__init__()
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        # Transferir el precio de compra de todos los artículos del carrito
        # del monedero del propietario del carrito al monedero del propietario del artículo.
        for item in self.items:
            item.owner.wallet.deposit(item.price)
            self.owner.wallet.withdraw(item.price)
            item.set_owner(self.owner)

        # Vaciar el contenido del carrito.
        self.items = []

# Requisitos
#   - El monto de compra de todos los ítems en el carrito (Cart#items) debe transferirse del monedero del propietario del carrito al monedero del propietario del ítem.
#   - Se debe transferir la propiedad de todos los ítems en el carrito (Cart#items) al propietario del carrito.
#   - El contenido del carrito (Cart#items) debe estar vacío.
# Sugerencias
#   - Monedero del propietario del carrito ==> self.owner.wallet
#   - Monedero del propietario del ítem ==> item.owner.wallet
#   - Transferir dinero implica ==> retirar la cantidad del monedero de (？) e ingresarla en el monedero de (？).
#   - Transferir la propiedad del ítem al propietario del carrito implica ==> reescribir el propietario (item.owner = ?)