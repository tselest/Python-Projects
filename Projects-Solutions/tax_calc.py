# Tax calculator


# TAX RATES PER STATES >>> https://taxfoundation.org/2020-sales-taxes/
# tax rates per EU COUNTRIES >>> https://taxfoundation.org/vat-rates-europe-2019/


tax_rates = { 'US State': { "AL": 0.0922, "AK": 0.0176 , "AZ": 0.084, 
             "AR": 0.0947, "CA" : 0.0866, "CO": 0.0765, 
             "CT": 0.0635, "DC": 0.06, "DE": 0,
             "FL": 0.0705, "GA": 0.0731, "HI": 0.0444, 
             "ID": 0.0603, "IL": 0.0908, "IN": 0.07, 
             "IA": 0.0964, "KS": 0.0868, "KY": 0.06, 
             "LA": 0.0952, "ME": 0.055, "MD": 0.06, 
             "MA": 0.0625, "MI": 0.0985, "MN": 0.0746, 
             "MS": 0.0707, "MO": 0.0818, "MT": 'N/A', 
             "NE": 0.0693, "NV": 0.0832, "NH": 0, 
             "NJ" : 0.1075, "NM": 0.0782, "NY": 0.0852, 
             "NC": 0.0697, "ND": 0.0686, "OH": 0.0717, 
             "OK": 0.0894, "OR" : 0, "PA": 0.0634, 
             "RI": 0.07 , "SC": 0.0746, "SD": 0.064, 
             "TN": 0.0953, "TX": 0.0819, "UT": 0.0718, 
             "VT": 0.0622, "VA": 0.0565, "WA": 0.0921, 
             "WY": 0.0534, "WI": 0.0546, "WV": 0.0641}, 

            'EU Country' : {'BE': 0.21, 'LU': 0.17, 
                            'SI': 0.22, 'GR': 0.24, 'TR': 0.18, 
                            'IT': 0.22, 'ES': 0.21, 'PT': 0.23, 
                            'FR': 0.2,  'HU': 0.27, 'DE': 0.19, 
                            'NL': 0.21, 'CH': 0.077,'IE': 0.23, 
                            'DK': 0.25, 'NO': 0.25, 'SE': 0.25, 
                            'FI': 0.24, 'IS': 0.24, 'LV': 0.21, 
                            'EE': 0.2,  'AT': 0.2,  'SK': 0.2, 
                            'CZ': 0.21, 'LT': 0.34, 'PL': 0.23 }}


print("Enter tax lookup \n \
1: EU Country \n \
2: US State")

def tax():
    tax_lookup = int(input())
    if tax_lookup == 1:
        choice = 'EU Country'
    elif tax_lookup ==2:
        choice = 'US State'
    else:
        return "Invalid Choice"

    cost = float(input("Enter Cost: "))
    rate = str(input(f"Select Tax Rate {','.join(tax_rates[choice].keys())}: "))

    while True:
        try:
            if rate not in ['MT' , 'NH', 'OR', 'DE']:
                return f"Cost of {cost:.2f} in {rate} is {float(cost + (cost * tax_rates[choice][rate])):.2f}"
            else:
                return f"Sorry, the tax rate for {rate} is not applicable."
            #break
        except KeyError:
            return "There was an error. Give a valid country/state."
            #break

if __name__=="__main__":
    print(tax())
