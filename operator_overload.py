class Bank():
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        return f"{self.dollars} dollars and {self.cents} cents."

    def __add__(self, other):
        dollars = self.dollars + other.dollars
        cents = self.cents + other.cents
        return Bank(dollars, cents)


def main():
    Sara = Bank(100, 100)
    Sy = Bank(50, 50)
    print(f"Sara: {Sara}\nSy: {Sy}\nTotal: {Sara+Sy}")


if __name__ == "__main__":
    main()
