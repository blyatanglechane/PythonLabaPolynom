class Polynomial:
    # хранилище коэффициентов и степеней
    StoreCoef = {}

    # ctrl + alt + L
    def __init__(self, *coefficients):
        self.coeff = coefficients
        self.SizeStore = len(self.coeff)
        SizeTuple = 0
        self.StoreCoef = {}
        for i in (self.coeff):
            if (isinstance(i, list)):
                self.StoreCoef = {}
                Size = 0
                for j in i:
                    self.StoreCoef[Size] = j
                    Size += 1
            if (isinstance(i, int)):
                self.StoreCoef[SizeTuple] = i
                SizeTuple += 1
            if (isinstance(i, dict)):
                self.StoreCoef = {}
                for key, value in i.items():
                    self.StoreCoef[key] = value
        self.current_index = 0  # текущий индекс для итерации по словарю
        self.items = list(self.StoreCoef.items())  # список пар ключ-значение из словаря

    def __repr__(self):
        ResultSt = "["
        Size = len(self.StoreCoef.items())
        for key, value in self.StoreCoef.items():
            if (Size - 1 != 0):
                ResultSt += str(value) + ", "
            else:
                ResultSt += str(value) + "]"
            Size -= 1
        return f"Polynomial {ResultSt}"

    def __str__(self):
        ResultSt = ""
        Size = len(self.StoreCoef.items())
        for key, value in reversed(self.StoreCoef.items()):
            # первый этап парсера
            if (value > 0 and Size != len(self.StoreCoef.items())):
                ResultSt += "+ "
            else:
                if (value < 0):
                    ResultSt += "- "
            # второй этап парсера
            if (value > 1 or value < -1 or ((abs(value) == 1) and key == 0)):
                ResultSt += str(abs(value))
            else:
                if (value == 0):
                    Size -= 1
                    continue
            # трейти этап парсера
            if (value != 0 and key != 0):
                ResultSt += "x"
            # четвёртый этап парсера
            if (key > 1 or key < 0):
                ResultSt += "^" + str(key)
            Size -= 1
            # пятый этап парсера
            if (Size > 0):
                ResultSt += " "
        return f"{ResultSt}"

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key, value in (other.StoreCoef.items()):
                if self.StoreCoef == other.StoreCoef:
                    return True
                return False

    def __add__(self, other):
        StoreResult = {}
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key, value in (other.StoreCoef.items()):
                if (key in self.StoreCoef.keys()):
                    StoreResult[key] = self.StoreCoef[key] + value
                else:
                    StoreResult[key] = value
            for key, value in (self.StoreCoef.items()):
                if (not (key in StoreResult)):
                    StoreResult[key] = value
        return StoreResult

    def __radd__(self, other):
        StoreResult = {}
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key, value in (self.StoreCoef.items()):
                if (key in other.StoreCoef.keys()):
                    if (other.StoreCoef[key] + value != 0):
                        StoreResult[key] = other.StoreCoef[key] + value
                else:
                    StoreResult[key] = value
            for key, value in (other.StoreCoef.items()):
                if (not (key in StoreResult)):
                    StoreResult[key] = value
        return StoreResult

    def __neg__(self):
        NegStoreCoef = {}
        for key, value in self.StoreCoef.items():
            NegStoreCoef[key] = -value
        return NegStoreCoef

    def __sub__(self, other):
        StoreResult = {}
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key, value in (other.StoreCoef.items()):
                if (key in self.StoreCoef.keys()):
                    StoreResult[key] = self.StoreCoef[key] - value
                else:
                    StoreResult[key] = -value
            for key, value in (self.StoreCoef.items()):
                if (not (key in StoreResult)):
                    StoreResult[key] = value
        return StoreResult

    def __rsub__(self, other):
        StoreResult = {}
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key, value in (self.StoreCoef.items()):
                if (key in other.StoreCoef.keys()):
                    StoreResult[key] = other.StoreCoef[key] - value
                else:
                    StoreResult[key] = -value
            for key, value in (other.StoreCoef.items()):
                if (not (key in StoreResult)):
                    StoreResult[key] = value
        return StoreResult

    def __call__(self, x):
        sum = 0
        for key, value in self.StoreCoef.items():
            if (key != 0):
                sum += ((value * x) ** key)
            else:
                sum += value * x
        return sum

    def degree(self):
        max = -(2 ** 63 - 1)
        for key, value in self.StoreCoef.items():
            if (key > max):
                max = key
        print(max)

    def der(self, d=1):
        cof = 0
        pow = 0
        ResultSt = ""
        if not (d in self.StoreCoef.keys()):
            raise TypeError("Такой степени нету")
        else:
            cof = d * self.StoreCoef[d]
            if (d != 0):
                pow = d - 1
            # первый шаг парсера
            if (cof > 1 or cof < -1 or (abs(cof) == 1 and pow == 0)):
                ResultSt += str(cof)
            else:
                if (cof == -1):
                    ResultSt += "-"
            # второй шаг парсера
            if (cof != 0 and pow != 0):
                ResultSt += "x"
            # третий шаг парсера
            if (pow != 1 and pow != 0):
                ResultSt += "^" + str(pow)
            # если строка пуста
            if (ResultSt == ""):
                ResultSt += "0"
        print(ResultSt)

    def __mul__(self, other):
        StoreResult = {}
        ResKey = 0
        ResValue = 0
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key1, value1 in (self.StoreCoef.items()):
                for key2, value2 in (other.StoreCoef.items()):
                    ResKey = key1 + key2
                    ResValue = value1 * value2
                    if (ResKey in StoreResult.keys()):
                        StoreResult[ResKey] += ResValue
                    else:
                        StoreResult[ResKey] = ResValue
        return StoreResult

    def __rmul__(self, other):
        StoreResult = {}
        ResKey = 0
        ResValue = 0
        if not isinstance(other, Polynomial):
            raise TypeError("Неверный тип данных")
        else:
            for key1, value1 in (other.StoreCoef.items()):
                for key2, value2 in (self.StoreCoef.items()):
                    ResKey = key1 + key2
                    ResValue = value1 * value2
                    if (ResKey in StoreResult.keys()):
                        StoreResult[ResKey] += ResValue
                    else:
                        StoreResult[ResKey] = ResValue
        return StoreResult

    # метод, позволяющий сделать объект итеративным
    def __iter__(self):
        self.current_power = 0
        return self

    # метод для возврата следующей пары ключ-значение из словаря
    # self.current_power не должен быть больше максимальной степени хранящейся в словаре
    def __next__(self):
        if self.current_power > max(self.StoreCoef.keys()):
            raise StopIteration
        else:
            value = self.StoreCoef.get(self.current_power, 0)  # получаем значение текущей степени из словаря
            self.current_power += 1
            return "(" + str(self.current_power - 1) + ", " + str(value) + ")"


pol = Polynomial([0])
pol1 = Polynomial([1, 2, 3])
pol2 = Polynomial({0: -3, 2: 1, 5: 4})
pol3 = Polynomial(0, 2, 0, 5)
pol4 = Polynomial({0: 1, 1: 2, 2: 3})

print(pol)
print(pol1)
print(pol2)
print(pol3)

print(pol1.__repr__())
print(pol2.__repr__())
print(pol3.__repr__())

print(pol1 == pol3)

print(pol1 + pol2)

print(-pol2)

print((pol3 - pol1))

print(pol3(1))

print(Polynomial(1, 2, 3))

pol1.degree()

pol3.der(1)

print(pol1 * pol2)

for i in pol2:
    print(i)
