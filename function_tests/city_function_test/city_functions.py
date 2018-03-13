
def city_country(city,country,population=''):
    city_n_county=city.title()+', '+country.title()
    if not population:
        return city_n_county
    return city_n_county +' - population '+ str(population)


print(city_country('nairobi','kenya',300000))
print(city_country('lagos','nigeria'))