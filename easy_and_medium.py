# # 1easy
#
# class Country:
#     pass
#
#
# class Russia(Country):
#
#     def __init__(self):
#         self.population = None
#
#     def set_population(self):
#         self.population = input('with population russia?')
#
#     def get_population(self):
#         print('population_of_russia')
#         print(self.population)
#
#
# class Canada(Country):
#
#     def __init__(self):
#         self.population = None
#
#     def set_population(self):
#         self.population = input('with population canada?')
#
#     def get_population(self):
#         print('population_of_canada')
#         print(self.population)
#
#
# class Germany(Country):
#
#     def __init__(self):
#         self.population = None
#
#     def set_population(self):
#         self.population = input('with population germany?')
#
#     def get_population(self):
#         print('population_of_germany')
#         print(self.population)
#
#
# russia = Russia()
# canada = Canada()
# germany = Germany()
#
# canada.set_population()
# canada.get_population()
#
# russia.set_population()
# russia.get_population()
#
# germany.set_population()
# germany.get_population()


# 2easy

# import json
#
# countries = ['Russia', 'Canada', 'Germany']
#
# f = open('list_of_countries.json', 'w')
# json.dump(countries, f)
# f.close()
#
# f = open('list_of_countries.json', 'r')
# list_countries = json.load(f)
# print(list_countries)
# f.close()



# 1medium

# class Soda:
#
#     def __init__(self, add):
#         self.add = add
#
#     def show_my_drink(self):
#         if self.add:
#             print('Soda and ' + self.add)
#         else:
#             print('Usually soda')
#
#
# soda1 = Soda('gooseberry')
# soda1.show_my_drink()
#
# soda2 = Soda(None)
# soda2.show_my_drink()


# 2medium

# class FlavourSoda:
#
#     def __enter__(self):
#         print('It is enter')
#         return self.get_add()
#
#     def __init__(self, add):
#         self.add = add
#
#     def get_add(self):
#         print('It is add:' + self.add)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('It is exit')
#
#
# with FlavourSoda('apple') as f:
#     pass


