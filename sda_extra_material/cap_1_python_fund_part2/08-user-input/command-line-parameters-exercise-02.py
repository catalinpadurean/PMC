import sys

country_capital_dict = {}

# Read country name and its capital name input separated by a comma
country_and_capital_names_input = sys.argv[1]
# Split user provided string into list using comma as delimiter ('Japan,Tokyo' -> ['Japan', 'Tokyo'])
country_and_capital_name_list = country_and_capital_names_input.split(",")

# Add country and its capital to the dictionary by accessing it in the list
country_capital_dict[country_and_capital_name_list[0]] = country_and_capital_name_list[1]

# Read country name and its capital name input separated by a comma
country_and_capital_names_input = sys.argv[2]
# Split user provided string into list using comma as delimiter ('Japan,Tokyo' -> ['Japan', 'Tokyo'])
country_and_capital_name_list = country_and_capital_names_input.split(",")

# Add country and its capital to the dictionary by accessing it in the list
country_capital_dict[country_and_capital_name_list[0]] = country_and_capital_name_list[1]

# Read country name and its capital name input separated by a comma
country_and_capital_names_input = sys.argv[3]
# Split user provided string into list using comma as delimiter ('Japan,Tokyo' -> ['Japan', 'Tokyo'])
country_and_capital_name_list = country_and_capital_names_input.split(",")

# Add country and its capital to the dictionary by accessing it in the list
country_capital_dict[country_and_capital_name_list[0]] = country_and_capital_name_list[1]

print(country_capital_dict)
