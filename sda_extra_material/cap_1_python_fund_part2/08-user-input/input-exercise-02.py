country_capital_dict = {}

# a. User should input country and its capital in one input, separated by a comma “Japan,Tokyo”.
country_and_capital_names_input = input("Enter country name and its capital name separated by a comma: ")
# b. Use string split(“,”) function to split the string into a list of 2 substrings - the country and the city.
# The split(“,”) function splits a string by a programmer defined delimiter into a list of substrings,
# for example: 'Japan,Tokyo' -> ['Japan', 'Tokyo']
country_and_capital_name_list = country_and_capital_names_input.split(",")

# Add country and its capital to the dictionary by accessing it in the list
country_capital_dict[country_and_capital_name_list[0]] = country_and_capital_name_list[1]

# a. User should input country and its capital in one input, separated by a comma “Japan,Tokyo”.
country_and_capital_names_input = input("Enter country name and its capital name separated by a comma: ")
# b. Use string split(“,”) function to split the string into a list of 2 substrings - the country and the city.
# The split(“,”) function splits a string by a programmer defined delimiter into a list of substrings,
# for example: 'Japan,Tokyo' -> ['Japan', 'Tokyo']
country_and_capital_name_list = country_and_capital_names_input.split(",")

# Add country and its capital to the dictionary by accessing it in the list
country_capital_dict[country_and_capital_name_list[0]] = country_and_capital_name_list[1]

# a. User should input country and its capital in one input, separated by a comma “Japan,Tokyo”.
country_and_capital_names_input = input("Enter country name and its capital name separated by a comma: ")
# b. Use string split(“,”) function to split the string into a list of 2 substrings - the country and the city.
# The split(“,”) function splits a string by a programmer defined delimiter into a list of substrings,
# for example: 'Japan,Tokyo' -> ['Japan', 'Tokyo']
country_and_capital_name_list = country_and_capital_names_input.split(",")

# Add country and its capital to the dictionary by accessing it in the list
country_capital_dict[country_and_capital_name_list[0]] = country_and_capital_name_list[1]

# c. Print out the resulting dictionary.
print(country_capital_dict)
