


# funkcija failo nuskaitymui

def read_data_from_file(filename):
    """
        Atidaro failą ir surašo duomenų eilutes į listą, kiekviena eilutė 
        taip pat talpinama į listą.

        Args.:
            filename: Kelias iki failo su failo pavadinimu, mano atveju failas yra darbinėj aplinkoj,
            todėl kelio nenurodau

        Return:
            gražina listą, kurio elementai yra listai sudaryti iš kiekvienos eilutės.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    data = []
    for i, line in enumerate(lines):

        # Praleidžiame pirmąją eilutę (stulpelių pavadinimus)
        if i == 0:  
            continue

        # išsivalau ir susiskaidau į elementus liste, pasiverčiu į int
        line_list = line.strip().split(',')
        line_list[0] = int(line_list[0])
        line_list[1] = int(line_list[1])
        line_list[2] = int(line_list[2])
        line_list[3] = int(line_list[3])
        data.append(line_list)

    return data

# Nuskaitome duomenis iš failo
data = read_data_from_file('data.txt')
 

#susikuriam tuščius listus į kuriuos talpinsiu duomenis
wrong_data = []
red_data = []   
yellow_data = []
green_data = []
red_activetime = []
yellow_activetime = []
green_activetime = []
green_avtive_times = []

# einam per kiekvieną nuskaityto failo eilute
for line in data:
    # pirma patikrinam ar eilutė yra tinkama, jei netinkama - itraukiam į wrong_data sarašą
    if  line[0] + line[1] + line[2] > 1 or line[0] + line[1] + line[2] < 1:
        wrong_data.append(line)
    else:
        # ieškoom elementų, kurie būtų lygūs 1, taip žinom, kad spalva buvo aktyvi ir itraukiam į atitinkamus listus kiekvienoj if sąlygoj
        if line[0] == 1:   
            red_data.append(line)
            red_activetime.append(int(line[3]))
        if line[1] == 1:   
            yellow_data.append(line)
            yellow_activetime.append(int(line[3]))
        if line[2] == 1:   
            green_data.append(line)
            green_activetime.append(int(line[3]))
            green_avtive_times.append(line[4])


def cycles_counting(data):
    """
    Suskaičiuoja, kiek kartų pasikartoja tam tikra seka (raudona, geltona, žalia, geltona, raudona) duomenyse.

    Args:
        data: Sąrašas sąrašų, kur kiekvienas vidinis sąrašas atitinka vieną duomenų eilutę 
              ir turi bent tris elementus: [red, yellow, green, ...].

    Returns:
        int: Kiek kartų seka pasikartoja duomenyse.
    """

    pattern_list = [1, 1, 1, 1, 1]  # Ieškoma paternas
    apperence_counter = 0 # pilnų ciklų skaičius
    counter = 0 # skaičiuos kiek kartų patikrinimas buvo teisingas

    for i in range(len(data)):
        if data[i][0] != 1:  # Praleidžiame eilutes, kur 'red' nėra 1
            continue

        if i == len(data) - 4:  # Patikriname, ar nepasibaigė duomenys, žemiau esančio indekso eilutė nebeišpildys pilno ciklo
            break

        for j, element in enumerate(pattern_list):
            idx_tmp = i + j  # Apskaičiuojame indeksą duomenų sąraše

            if element == data[idx_tmp][0]:  # Tikriname 'red'
                counter += 1
            elif element == data[idx_tmp][1]:  # Tikriname 'yellow'
                counter += 1
            elif element == data[idx_tmp][2]:  # Tikriname 'green'
                counter += 1
            else:
                break  # Jei seka nesutampa, nutraukiame vidinį ciklą

        if counter == 5:  # Jei visa seka sutapo - irašome apperence_counter +1, ciklas užfiksuotas
            apperence_counter += 1
            counter = 0 # nuresetinam patikriniumus ir einam iš naujo

    return apperence_counter



# Sukuriame naują failą ir įrašome tekstą
with open('rezultatai.txt', 'w', encoding='utf-8') as file:
    file.write(f'raudona spalva pasirodė: {len(red_data)} kartus\n') 
    file.write(f'geltona spalva pasirodė: {len(yellow_data)} kartus\n') 
    file.write(f'žalia spalva pasirodė: {len(green_data)} kartus\n')

    file.write(f'raudona spalva aktyvi buvo: {sum(red_activetime)} sekundes\n')
    file.write(f'geltona spalva aktyvi buvo: {sum(yellow_activetime)} sekundes\n')
    file.write(f'žalia spalva aktyvi buvo: {sum(green_activetime)} sekundes\n')

    file.write(f'žalia spalvos visi laikai: {green_avtive_times}\n')
    file.write(f'Pilni spalvų ciklai (raudona, geltona, žalia, geltona, raudona): {cycles_counting(data)} kartų\n')
    file.write(f'Eilučių skaičius su klaidingais duomenimis: {len(wrong_data)}\n')