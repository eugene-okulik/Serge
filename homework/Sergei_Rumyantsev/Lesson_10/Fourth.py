PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

step = PRICE_LIST.split('\n')

result_dict = {price.split()[0]: int(price.split()[1].strip('р')) for price in step}
print(result_dict)
