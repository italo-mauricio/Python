from countryinfo import CountryInfo


countrys = CountryInfo(input("Digite o nome do país: "))

print(f'''

    País: {countrys.name()}
    Capital: {countrys.capital()}
    Moedas: {countrys.currencies()}
    Idiomas: {countrys.languages()}
    Fronteiras: {countrys.borders()}
    DDD: {countrys.calling_codes()}
    População: {countrys.population()}



''')