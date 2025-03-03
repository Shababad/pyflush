class Player():
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

        self.cards = []
        self.allin = False
        self.folded = False
        self.round_stake = 0
        self.total_stake = 0

    def bal(self, amount):
        self.balance += amount

    def stake(self, amount):
        self.round_stake += amount
        self.total_stake += amount

    def decide(self, bet, log) -> tuple[str, int | None]:

        required: int = bet - self.round_stake
        actions: list = ["fold", "all_in"]
        amount: int = None

        # Valid actions
        if required > 0 and required < self.balance:
            actions.append("call")
            actions.append("raise")
        elif required == 0:
            actions.append("check")
            actions.append("bet")

        print("Your turn")
        print(f"Possible actions: {actions}")
        print(f"Balance: {self.balance}")
        print(f"Required: {required}")
        print(f"Your Cards: {[card.name for card in self.cards]}")

        action = input("Action: ")
        while action not in actions:
            action = input(f"You cannot {action}, try again: ")
        if action.lower() in ["raise", "bet"]:
            amount = int(input(f"{action} amount: "))
            while amount > self.balance:
                amount = input(f"{amount} is greater than your balance, do you want to go all-in? [y/n]: ")
                if amount == "y":
                    return "all_in"
                else:
                    amount = int(input(f"{action} amount: "))
                    
        while action == "all_in":
            verify = input(f"Are you sure you want to go all in with {self.balance}? [y/n]: ")
            if verify == "y":
                return "all_in"
            else:
                action = input("New action: ")
        while action == "fold":
            verify = input(f"Are you sure you want to fold with {self.cards}? [y/n]: ")
            if verify == "y":
                return "fold"
            else:
                action = input("New action: ")


        return action, amount
