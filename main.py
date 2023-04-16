class Polynomial:
    # ctrl + alt + L
    def __init__(self, *coefficients):
        self.coeff = coefficients
        self.SizeStore = len(self.coeff)
        size_tuple = 0
        self.store_coef = {}
        for index in self.coeff:
            if isinstance(index, list):
                self.store_coef = {}
                size = 0
                for j in index:
                    self.store_coef[size] = j
                    size += 1
            if isinstance(index, int):
                self.store_coef[size_tuple] = index
                size_tuple += 1
            if isinstance(index, dict):
                self.store_coef = {}
                for key, value in index.items():
                    self.store_coef[key] = value
        self.current_index = 0  # текущий индекс для итерации по словарю
        self.items = list(self.store_coef.items())  # список пар ключ-значение из словаря

    def __repr__(self):
        result_st = "["
        size = len(self.store_coef.items())
        for key, value in self.store_coef.items():
            if size - 1 != 0:
                result_st += str(value) + ", "
            else:
                result_st += str(value) + "]"
            size -= 1
        return f"Polynomial {result_st}"

    def __str__(self):
        result_st = ""
        size = len(self.store_coef.items())
        for key, value in reversed(self.store_coef.items()):
            # первый этап парсера
            if value > 0 and size != len(self.store_coef.items()):
                result_st += "+ "
            else:
                if value < 0:
                    result_st += "- "
            # второй этап парсера
            if value > 1 or value < -1 or ((abs(value) == 1) and key == 0):
                result_st += str(abs(value))
            else:
                if value == 0:
                    size -= 1
                    continue
            # трейти этап парсера
            if value != 0 and key != 0:
                result_st += "x"
            # четвёртый этап парсера
            if key > 1 or key < 0:
                result_st += "^" + str(key)
            size -= 1
            # пятый этап парсера
            if size > 0:
                result_st += " "
        return f"{result_st}"

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            if self.store_coef == other.store_coef:
                return True
            return False

    def __add__(self, other):
        store_result = {}
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key, value in other.store_coef.items():
                if key in self.store_coef.keys():
                    store_result[key] = self.store_coef[key] + value
                else:
                    store_result[key] = value
            for key, value in self.store_coef.items():
                if not (key in store_result):
                    store_result[key] = value
        return Polynomial(store_result)

    def __radd__(self, other):
        store_result = {}
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key, value in self.store_coef.items():
                if key in other.store_coef.keys():
                    if other.store_coef[key] + value != 0:
                        store_result[key] = other.store_coef[key] + value
                else:
                    store_result[key] = value
            for key, value in other.store_coef.items():
                if not (key in store_result):
                    store_result[key] = value
        return Polynomial(store_result)

    def __neg__(self):
        neg_store_coef = {}
        for key, value in self.store_coef.items():
            neg_store_coef[key] = -value
        return Polynomial(neg_store_coef)

    def __sub__(self, other):
        store_result = {}
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key, value in other.store_coef.items():
                if key in self.store_coef.keys():
                    store_result[key] = self.store_coef[key] - value
                else:
                    store_result[key] = -value
            for key, value in self.store_coef.items():
                if not (key in store_result):
                    store_result[key] = value
        return Polynomial(store_result)

    def __rsub__(self, other):
        store_result = {}
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key, value in self.store_coef.items():
                if key in other.store_coef.keys():
                    store_result[key] = other.store_coef[key] - value
                else:
                    store_result[key] = -value
            for key, value in other.store_coef.items():
                if not (key in store_result):
                    store_result[key] = value
        return Polynomial(store_result)

    def __call__(self, x):
        summa: int = 0
        for key, value in self.store_coef.items():
            if key != 0:
                summa += (value * x) ** key
            else:
                summa += value * x
        return summa

    def degree(self):
        maxim = -(2 ** 63 - 1)
        for key, value in self.store_coef.items():
            if key > maxim:
                maxim = key
        print(maxim)

    def der(self, d=1):
        deg = 0
        result_st = ""
        if not (d in self.store_coef.keys()):
            raise TypeError("Такой степени нету")
        else:
            cof = d * self.store_coef[d]
            if d != 0:
                deg = d - 1
            # первый шаг парсера
            if cof > 1 or cof < -1 or (abs(cof) == 1 and deg == 0):
                result_st += str(cof)
            else:
                if cof == -1:
                    result_st += "-"
            # второй шаг парсера
            if cof != 0 and deg != 0:
                result_st += "x"
            # третий шаг парсера
            if deg != 1 and deg != 0:
                result_st += "^" + str(deg)
            # если строка пуста
            if result_st == "":
                result_st += "0"
        print(result_st)

    def __mul__(self, other):
        store_result = {}
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key1, value1 in self.store_coef.items():
                for key2, value2 in other.store_coef.items():
                    res_key = key1 + key2
                    res_value = value1 * value2
                    if res_key in store_result.keys():
                        store_result[res_key] += res_value
                    else:
                        store_result[res_key] = res_value
        return Polynomial(store_result)

    def __rmul__(self, other):
        store_result = {}
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key1, value1 in other.store_coef.items():
                for key2, value2 in self.store_coef.items():
                    res_key = key1 + key2
                    res_value = value1 * value2
                    if res_key in store_result.keys():
                        store_result[res_key] += res_value
                    else:
                        store_result[res_key] = res_value
        return Polynomial(store_result)

    # метод, позволяющий сделать объект итеративным
    def __iter__(self):
        self.current_power = 0
        return self

    # метод для возврата следующей пары ключ-значение из словаря
    # self.current_power не должен быть больше максимальной степени хранящейся в словаре
    def __next__(self):
        if self.current_power > max(self.store_coef.keys()):
            raise StopIteration
        else:
            value = self.store_coef.get(
                self.current_power, 0
            )  # получаем значение текущей степени из словаря
            self.current_power += 1
            return "(" + str(self.current_power - 1) + ", " + str(value) + ")"


pol1 = Polynomial(1)
pol2 = Polynomial({0: -3, 2: 1, 5: 4})
pol3 = Polynomial(0, 2, 0, 5)
pol4 = Polynomial({0: 1, 1: 2, 2: 3})

print(pol1)
print(pol2)
print(pol3)
print(pol4)

print(pol1.__repr__())
print(pol2.__repr__())
print(pol3.__repr__())

print(pol1 == pol3)

print(pol1 + pol2)

print(-pol2)

print((pol3 - pol1))

print(pol3(1))

pol1.degree()

pol3.der(1)

print(pol1 * pol2)

for i in pol2:
    print(i)
