def harry(wand, potter):
    print(f'{potter}, {wand}')
    spell = confundo(wand + potter * 10)
    print(f'{potter}, {spell}, {wand}')
    wand = potter
    if spell > 1.5:
        if spell < 2.0:
            return 10
    elif spell > 1.3:
        return 30
    else:
        return 40
    return 50

def confundo(wand):
    print(wand)
    return wand / 10

def main():
    potter = 1
    wand = potter + 1
    print(f'{potter}, {wand}')
    potter = harry(potter, wand) + potter
    print(f'{potter}, {wand}')

main()
