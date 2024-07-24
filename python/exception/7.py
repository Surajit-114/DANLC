
class OutOfStockError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidOrderError(Exception):
    def __init__(self, message):
        super().__init__(message)


def process_order(order, stock):
    for item, quantity in stock.items():
        if quantity == 0:
            raise OutOfStockError(f"{item} is out of stock!!")

    for item, quantity in order.items():
        if quantity <= 0:
            raise InvalidOrderError(f"Inavlid order quantity for {item}")


def main():
    order = {"apple": 5, "banana": 3, "cherry": 10}
    stock = {"apple": 20, "banana": 15, "cherry": 8, "date": 25}
    try:
        process_order(order, stock)
    except (OutOfStockError, InvalidOrderError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
