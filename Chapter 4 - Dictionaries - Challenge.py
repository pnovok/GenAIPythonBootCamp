# Challenge #1
#Write a Python script that removes all duplicate elements from a list in a single line using sets.
import numbers

my_list = [1,2,'abc',2,2,4]

set1 = {item for item in my_list}
print(set1)
print(my_list)

#Another solution
my_list = list(set(my_list))
print(my_list)

# Challenge #2
# Write a Python script that counts and displays the occurrences of each character in a list.

my_list2 = list('mamma mia mm')
print(my_list2)

my_list2_unique = list(set(my_list2))
print(my_list2_unique)

for letter in my_list2_unique:
    print(f"{letter}  --->  {my_list2.count(letter)}")

#Another solution
l1 = list('mama mia mm')
tmp_list = list()
for item in set(l1):
    count = l1.count(item)
    tmp_list.append((item, count))

# sort list by the second element of the tuple
tmp_list.sort(key=lambda x:x[1], reverse=True)
# print(tmp_list)

for item in tmp_list:
    print(f'{item[0]} ---> {item[1]}')

#Challenge #3
#Given a list of words, write a Python script that creates a dictionary where each word is a key, and its length is the value.
#Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
#Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}

words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

def produce_dict(words):
    dict = {}
    for word in words:
        dict[word] = len(word)
    print(dict)

produce_dict(words)


#Challenge #4

#Considering the following dict, get a dict representation sorted by key.
#d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
#A dict representation means viewing or printing the dict.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

sorted_dict = dict(sorted(d1.items()))
print(sorted_dict)

# Another solution

for k in sorted(d1.keys()):
    print(f'{k} -> {d1[k]}')

#Challenge #5

#Considering the following dict, get a dict representation sorted by value.
#A dict representation means viewing or printing the dict.

d2 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

sorted_by_value = dict(sorted(d2.items(), key=lambda item: item[1]))
print(sorted_by_value)

x = True
y = False
z = True
print(x and not y or z)

# Challenge #6
# Let's generalize the last challenge and sort a dictionary by any field of its values if the value is a composite type (list, tuple, etc).
# Example:
# Considering this dictionary, print a sorted view of the dictionary by the second field of its values.
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Diana', ('NYC', 3500, 31)), ('Maria', ('Zagreb', 3800, 40)), ('John', ('London', 4000, 28))]
# P.S. Do it with a single line of code.

employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
sorted_employees = dict(sorted(employees.items(), key=lambda item: item[1][1]))
print(sorted_employees)

# Challenge #7
# Considering this dictionary, print a sorted view of the dictionary by the third field of its values, in reverse order.
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Maria', ('Zagreb', 3800, 40)), ('Diana', ('NYC', 3500, 31)), ('John', ('London', 4000, 28))]
# P.S. Do it with a single line of code.

employees2 = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
sorted_employees2 = dict(sorted(employees2.items(), key=lambda item: item[1][2], reverse=True))
print(sorted_employees2)

# Challenge #8
# Consider the dictionary called COUNTRY declared in this Python script.
# The keys are the country codes and the values are the country names.
# Print a sorted view of the dictionary, by the key (country code).

COUNTRY = {
"MX":"MEXICO",
"RW":"RWANDA",
"BI":"BURUNDI",
"PR":"PUERTO RICO",
"GM":"GAMBIA",
"SR":"SURINAME",
"KG":"KYRGYZSTAN",
"GA":"GABON",
"CK":"COOK ISLANDS",
"VN":"VIET NAM",
"UZ":"UZBEKISTAN",
"BG":"BULGARIA",
"JP":"JAPAN",
"KP":"KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
"PL":"POLAND",
"BB":"BARBADOS",
"CF":"CENTRAL AFRICAN REPUBLIC",
"GI":"GIBRALTAR",
"AE":"UNITED ARAB EMIRATES",
"MY":"MALAYSIA",
"KI":"KIRIBATI",
"RU":"RUSSIAN FEDERATION",
"MQ":"MARTINIQUE",
"SB":"SOLOMON ISLANDS",
"TL":"TIMOR-LESTE",
"VI":"VIRGIN ISLANDS, U.S.",
"FR":"FRANCE",
"ZA":"SOUTH AFRICA",
"NE":"NIGER",
"IE":"IRELAND",
"MG":"MADAGASCAR",
"TC":"TURKS AND CAICOS ISLANDS",
"BW":"BOTSWANA",
"KY":"CAYMAN ISLANDS",
"JO":"JORDAN",
"MR":"MAURITANIA",
"NI":"NICARAGUA",
"KM":"COMOROS",
"FK":"FALKLAND ISLANDS (MALVINAS)",
"SH":"SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA",
"PF":"FRENCH POLYNESIA",
"DK":"DENMARK",
"PT":"PORTUGAL",
"NR":"NAURU",
"DM":"DOMINICA",
"GH":"GHANA",
"GP":"GUADELOUPE",
"CU":"CUBA",
"GR":"GREECE",
"AS":"AMERICAN SAMOA",
"AI":"ANGUILLA",
"LS":"LESOTHO",
"TJ":"TAJIKISTAN",
"AW":"ARUBA",
"GY":"GUYANA",
"LC":"SAINT LUCIA",
"GG":"GUERNSEY",
"TG":"TOGO",
"OM":"OMAN",
"NL":"NETHERLANDS",
"MT":"MALTA",
"MD":"MOLDOVA, REPUBLIC OF",
"EC":"ECUADOR",
"FM":"MICRONESIA, FEDERATED STATES OF",
"CA":"CANADA",
"TT":"TRINIDAD AND TOBAGO",
"CN":"CHINA",
"CM":"CAMEROON",
"BD":"BANGLADESH",
"LK":"SRI LANKA",
"CO":"COLOMBIA",
"LT":"LITHUANIA",
"DJ":"DJIBOUTI",
"CX":"CHRISTMAS ISLAND",
"TF":"FRENCH SOUTHERN TERRITORIES",
"TM":"TURKMENISTAN",
"SC":"SEYCHELLES",
"MK":"MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF",
"TH":"THAILAND",
"LA":"LAO PEOPLE'S DEMOCRATIC REPUBLIC",
"BE":"BELGIUM",
"UY":"URUGUAY",
"MV":"MALDIVES",
"SZ":"SWAZILAND",
"MN":"MONGOLIA",
"PK":"PAKISTAN",
"BZ":"BELIZE",
"AT":"AUSTRIA",
"WF":"WALLIS AND FUTUNA",
"GD":"GRENADA",
"RO":"ROMANIA",
"SJ":"SVALBARD AND JAN MAYEN",
"CV":"CAPE VERDE",
"UG":"UGANDA",
"CR":"COSTA RICA",
"HM":"HEARD ISLAND AND MCDONALD ISLANDS",
"TN":"TUNISIA",
"MC":"MONACO",
"MP":"NORTHERN MARIANA ISLANDS",
"SN":"SENEGAL",
"PW":"PALAU",
"VC":"SAINT VINCENT AND THE GRENADINES",
"ST":"SAO TOME AND PRINCIPE",
"DO":"DOMINICAN REPUBLIC",
"EG":"EGYPT",
"TZ":"TANZANIA, UNITED REPUBLIC OF",
"SV":"EL SALVADOR",
"TR":"TURKEY",
"SG":"SINGAPORE",
"UM":"UNITED STATES MINOR OUTLYING ISLANDS",
"KR":"KOREA, REPUBLIC OF",
"PG":"PAPUA NEW GUINEA",
"GQ":"EQUATORIAL GUINEA",
"US":"UNITED STATES",
"BF":"BURKINA FASO",
"AM":"ARMENIA",
"TD":"CHAD",
"NP":"NEPAL",
"IT":"ITALY",
"IO":"BRITISH INDIAN OCEAN TERRITORY",
"ZW ":"ZIMBABWE",
"HU":"HUNGARY",
"BR":"BRAZIL",
"IN":"INDIA",
"PH":"PHILIPPINES",
"TW":"TAIWAN, PROVINCE OF CHINA",
"AO":"ANGOLA",
"MH":"MARSHALL ISLANDS",
"NO":"NORWAY",
"JE":"JERSEY",
"VU":"VANUATU",
"EE":"ESTONIA",
"AF":"AFGHANISTAN",
"AX":"ALAND ISLANDS",
"GN":"GUINEA",
"FO":"FAROE ISLANDS",
"SE":"SWEDEN",
"SL":"SIERRA LEONE",
"LB":"LEBANON",
"MO":"MACAO",
"IR":"IRAN, ISLAMIC REPUBLIC OF",
"CG":"CONGO",
"SM":"SAN MARINO",
"NA":"NAMIBIA",
"CI":"COTE D'IVOIRE",
"GL":"GREENLAND",
"VE":"VENEZUELA, BOLIVARIAN REPUBLIC OF",
"VG":"VIRGIN ISLANDS, BRITISH",
"BH":"BAHRAIN",
"ZM":"ZAMBIA",
"HR":"CROATIA",
"MZ":"MOZAMBIQUE",
"KW":"KUWAIT",
"MA":"MOROCCO",
"DZ":"ALGERIA",
"AQ":"ANTARCTICA",
"AU":"AUSTRALIA",
"PN":"PITCAIRN",
"QA":"QATAR",
"AL":"ALBANIA",
"BN":"BRUNEI DARUSSALAM",
"NZ":"NEW ZEALAND",
"SA":"SAUDI ARABIA",
"RE":"REUNION",
"HK":"HONG KONG",
"CD":"CONGO, THE DEMOCRATIC REPUBLIC OF THE",
"MW":"MALAWI",
"CZ":"CZECH REPUBLIC",
"DE":"GERMANY",
"AD":"ANDORRA",
"LU":"LUXEMBOURG",
"CY":"CYPRUS",
"TO":"TONGA",
"FJ":"FIJI",
"GT":"GUATEMALA",
"LV":"LATVIA",
"ES":"SPAIN",
"SI":"SLOVENIA",
"IM":"ISLE OF MAN",
"BS":"BAHAMAS",
"RS":"SERBIA",
"WS":"SAMOA",
"NC":"NEW CALEDONIA",
"SY":"SYRIAN ARAB REPUBLIC",
"MS":"MONTSERRAT",
"GB":"UNITED KINGDOM",
"PM":"SAINT PIERRE AND MIQUELON",
"CL":"CHILE",
"MF":"SAINT MARTIN",
"SO":"SOMALIA",
"BJ":"BENIN",
"YE":"YEMEN",
"TV":"TUVALU",
"GE":"GEORGIA",
"BM":"BERMUDA",
"GS":"SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS",
"AN":"NETHERLANDS ANTILLES",
"BY":"BELARUS",
"FI":"FINLAND",
"BV":"BOUVET ISLAND",
"LR":"LIBERIA",
"KH":"CAMBODIA",
"LY":"LIBYAN ARAB JAMAHIRIYA",
"MU":"MAURITIUS",
"GU":"GUAM",
"ER":"ERITREA",
"LI":"LIECHTENSTEIN",
"SD":"SUDAN",
"PA":"PANAMA",
"IL":"ISRAEL",
"EH":"WESTERN SAHARA",
"KE":"KENYA",
"CC":"COCOS (KEELING) ISLANDS",
"IS":"ICELAND",
"GF":"FRENCH GUIANA",
"MM":"MYANMAR",
"HT":"HAITI",
"NF":"NORFOLK ISLAND",
"ML":"MALI",
"PY":"PARAGUAY",
"KZ":"KAZAKHSTAN",
"CH":"SWITZERLAND",
"BA":"BOSNIA AND HERZEGOVINA",
"BO":"BOLIVIA, PLURINATIONAL STATE OF",
"UA":"UKRAINE",
"BL":"SAINT BARTHELEMY",
"AZ":"AZERBAIJAN",
"BT":"BHUTAN",
"VA":"HOLY SEE (VATICAN CITY STATE)",
"PE":"PERU",
"AR":"ARGENTINA",
"TK":"TOKELAU",
"AG":"ANTIGUA AND BARBUDA",
"KN":"SAINT KITTS AND NEVIS",
"PS":"PALESTINIAN TERRITORY, OCCUPIED",
"ID":"INDONESIA",
"GW":"GUINEA-BISSAU",
"HN":"HONDURAS",
"NG":"NIGERIA",
"IQ":"IRAQ",
"JM":"JAMAICA",
"NU":"NIUE",
"ET":"ETHIOPIA",
"ME":"MONTENEGRO",
"SK":"SLOVAKIA",
"YT":"MAYOTTE"
}

keys = sorted(COUNTRY.keys())

for k in keys:
    print(f'{k} --> {COUNTRY[k]}')

# Challenge #10
# Given two lists storing company sales data:
# years = [2015, 2016, 2017, 2018, 2019, 2020]
# sales = [350000, 400000, 410000, 439000, 500000, 290000]
# Create a list of tuples pairing each year with its corresponding sales.
# Output:
# [(2015, 350000), (2016, 400000), (2017, 410000), (2018, 439000), (2019, 500000), (2020, 290000)]

years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [350000, 400000, 410000, 439000, 500000, 290000]
sales_list = list(zip(years, sales))
print(sales_list)

# Challenge #11
# Consider the following two Python Lists that save information about company sales for the last 6 years:
# years = [2015, 2016, 2017, 2018, 2019, 2020]
# sales = [350000, 400000, 410000, 439000, 500000, 290000]
# Create a new dictionary that has the keys, the years, and the values, the sales.
# The resulting dict should be:
# {2015: 350000, 2016: 400000, 2017: 410000, 2018: 439000, 2019: 500000, 2020: 290000}
years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [350000, 400000, 410000, 439000, 500000, 290000]

sales_dict = dict(zip(years, sales))
print(sales_dict)

# Challenge #12
# Consider the dictionary from the previous challenge.
# Create a new dictionary called profit, where the profit is 25% of sales.
# Use dictionary comprehension if possible.
# profit margin is 25%
profit = {k: v*0.25 for k, v in sales_dict.items()}
print(profit)

# Challenge #12
# Consider the following two lists:
# names = ["Dan", "John", "Diana"]
# phones = [11111, 2222, 3333]
# Create a set that contains the elements of the 2 lists in pairs.
# The resulting set should be: {('John', 2222), ('Diana', 3333), ('Dan', 11111)}
names = ["Dan", "John", "Diana"]
phones = [11111, 2222, 3333]
result_set = set(zip(names,phones))
print(result_set)