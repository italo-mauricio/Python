from countryinfo import CountryInfo

while True:
    countrys = CountryInfo(input("Digite o nome do país: "))
    cont = 0
    print(f'''

        País: {countrys.name()}
        Capital: {countrys.capital()}
        Moedas: {countrys.currencies()}
        Idiomas: {countrys.languages()}
        Fronteiras: {countrys.borders()}
        DDD: {countrys.calling_codes()}
        População: {countrys.population()}

    ''')

    conti = input("Deseja consultar novamente? [S/N] ")
    if conti == 'S' or conti == 's':
        cont += 1
    if conti == 'N' or conti == 'n':
        print("Thank You!")
        break
    