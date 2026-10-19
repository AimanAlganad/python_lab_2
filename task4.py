import xml.dom.minidom as minidom


def task4():
    dom = minidom.parse('currency.xml')
    currencies = dom.getElementsByTagName('Valute')

    result = {}

    for currency in currencies:
        code = currency.getElementsByTagName('CharCode')[0].firstChild.data
        nominal = currency.getElementsByTagName('Nominal')[0].firstChild.data

        result[code] = nominal

    print(result)


task4()
