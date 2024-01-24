class Cliente:
    def __init__(self, name, cpf, birth_date, salary, phone, adress):
        self._name = name
        self._cpf = cpf
        self._birth_date = birth_date
        self._phone = phone
        self._adress = adress
        self._salary = salary
        try:
            self._salary = float(salary)
            if self._salary < 0:
                raise ValueError("Salary cannot be negative")
        except ValueError:
            raise ValueError("Invalid salary")
