formula_carbon_prefix = ['мет', 'эт', 'проп', 'бут', 'пент', 'гекс', 'гепт', 'окт', 'нон']
formula_hydroc_suffix = ['', 'ди', 'три']

def priks(formula: str):
    formula = formula.lower().replace('(', '').replace(')', '')
    if formula == 'c6h6':
        return 'бензол'
    if formula[0] == 'c' and (formula[2] == 'h' or formula[1] == 'h'):
        hydroc_count = ''
        if formula[1].isdigit():
            carbon_count = int(formula[1]) - 1
        else:
            carbon_count = 0
        prefix = formula_carbon_prefix[carbon_count]
        if 'o' in formula:
            oxygen = formula.split('o')
            if oxygen[1] == '':
                oxygen_count = 1
            else:
                oxygen_count = int(oxygen[1])
        carbon_count += 1
        if formula[2] == 'h' or formula[1] == 'h':
            suffix = ''
            if carbon_count > 1:
                hydrogen = formula.replace(f'c{carbon_count}', '')
            else:
                hydrogen = formula.replace(f'c', '')
            if 'o' in formula:
                if oxygen_count > 1:
                    hydrogen = hydrogen.replace(f'o{oxygen_count}', '')
                else:
                    hydrogen = hydrogen.replace(f'o', '')
            if hydrogen.replace('h', '').replace('o', '') != '':
                hydro_count = int(hydrogen.replace('h', '').replace('o', '').replace(f'c', ''))
            else:
                hydro_count = 1
            if carbon_count / (hydro_count + 2) == 1/2 and 'o' not in formula:
                if carbon_count >= 3:
                    return (prefix+"ин (алкин)", prefix+"адиен (алкадиен)", 'цикло'+prefix+'ен' + " (циклоалкен)")
                elif carbon_count == 2:
                    suffix = 'ин'
            if hydro_count > 2:
                if carbon_count / (hydro_count - 2) == 1/2 and 'o' not in formula:
                    suffix = "ан"
            if hydro_count > 1:
                if carbon_count / (hydro_count - 1) == 1/2 and 'o' not in formula:
                    suffix = "ил"
            if carbon_count / (hydro_count) == 1/2:
                suffix = "ен"
                if carbon_count >= 3 and 'o' not in formula:
                    return (prefix+suffix+" (алкeн)", 'цикло'+prefix+'ан' + " (циклоалкан)")
        if 'o' in formula:
            if hydro_count > 2:
                if carbon_count / (hydro_count - 2) == 1/2:
                    return prefix + "ан" + formula_hydroc_suffix[oxygen_count-1] + "ол (спирт)"
            if oxygen_count == 1:
                if suffix == 'ен':
                    if carbon_count > 2:
                        return (prefix+'аналь' + " (альдегид)", prefix+'анон' + " (кетон)")
                    elif carbon_count == 2:
                        return prefix+'аналь' + " (альдегид)"
            elif oxygen_count == 2:
                if suffix == 'ен':
                    suffix = "ановая кислота"
                    return prefix + suffix
        if suffix != '' and 'o' not in formula:
            if suffix == 'ин':
                suffix += " (алкин)"
            elif suffix == 'ан':
                suffix += " (алкан)"
            elif suffix == 'ен':
                suffix += " (алкен)"
            return prefix + suffix
    if formula[0] == 'h':
        if formula == "hcooh":
            return 'метановая кислота'
        

if __name__ == "__main__":
    while True:
        print(priks(input()))
