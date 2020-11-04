product = [(1, {"название": "Память", "цена": 600, "количество": 10, "eд": "шт."}),
           (2, {"название": "Мат.плата", "цена": 3000, "количество": 5, "eд": "шт."}),
           (3, {"название": "Процессор", "цена": 10000, "количество": 5, "eд": "шт."}),
           ]

count = int(input("Введите сколько товаров будет вводится: "))


for i in  range(count):
      number = product[len(product)-1][0]+1
      print("Товар,{} из {}".format(i+1,count))
      model = {}
      model["название"] = input("Введите название продукта: ")
      model["цена"] = int(input("Введите цену продукта: "))
      model["количество"] = int(input("Введите количество продукта: "))
      model["eд"] = input("Введите ед. измерения продукта: ")
      
      prod = (number,model)
      product.append(prod)


analits = {}
for val in product:
    for k,v in val[1].items():
        if k in analits:
            analits[k].append(v)
            if k == "eд":
                analits[k] = list(set(analits[k]))
        else:
            analits[k] = [v]


for k,v in analits.items():
    print(k,v)