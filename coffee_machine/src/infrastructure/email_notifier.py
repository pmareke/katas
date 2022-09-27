from coffee_machine.src.domain.notifier import Notifier


class EmailNotifier(Notifier):

    def notify_missing_drink(self, drink: str) -> None:
        pass
