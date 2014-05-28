import random

firstV = ['A', 'E', 'I', 'O', 'U']
firstC = ['B', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T',
          'V', 'Z', 'Zh', 'Ch', 'Sh']
laterC = ['b', 'f', 'g', 'h', 'j', 'v', 'ch', 'sh', 'r', 's', 'zh', 'k', 'n',
          'm', 't', 'd', 'l', 'p']
laterVC = ['ab', 'ad', 'af', 'ag', 'aj', 'ak', 'al', 'am', 'an', 'ar', 'at',
           'av', 'azh', 'ash', 'ach', 'ed', 'eg', 'em', 'en', 'er', 'et', 'ev',
           'ob', 'od', 'os', 'og', 'oj', 'ok', 'ol', 'om', 'on', 'or', 'ot',
           'ov', 'oz', 'id', 'ik', 'il', 'ir', 'it', 'iv', 'is', 'iz', 'ub',
           'ud', 'uk', 'ul', 'um', 'un', 'up', 'ur', 'us', 'ut', 'ush', 'uzh',
           'uch', 'uv']
finalV = ['a', 'o', 'u', 'y']

def namer():
    syllable = random.randint(2, 4)
    VorC = random.randint(0, 1)
    if VorC == 0:
        fV = random.choice(firstV)
        lC = random.choice(laterC)
        if syllable == 2:
            eVorC = random.randint(0, 1)
            if eVorC == 0:
                eV = random.choice(finalV)
                return fV+lC+eV
            else:
                eC = random.choice(laterVC)
                return fV+lC+eC
        elif syllable == 3:
            mVorC = random.randint(0, 1)
            if mVorC == 0:
                mC = random.choice(laterC)
                eC = random.choice(laterVC)
                return fV+lC+mC+eC
            else:
                mV = random.choice(laterVC)
                eV = random.choice(finalV)
                return fV+lC+mV+eV
        else:
            mV = random.choice(laterVC)
            mC = random.choice(laterC)
            oV = random.choice(laterVC)
            eVorC = random.randint(0, 1)
            if eVorC == 0:
                eV = random.choice(finalV)
                return fV+lC+mV+mC+oV+eV
            else:
                eC = random.choice(laterVC)
                return fV+lC+mV+mC+oV+eC
    else:
        fC = random.choice(firstC)
        lV = random.choice(laterVC)
        if syllable == 2:
            eVorC = random.randint(0, 1)
            if eVorC == 0:
                eV = random.choice(finalV)
                return fC+lV+eV
            else:
                eC = random.choice(laterVC)
                return fC+lV+eC
        elif syllable == 3:
            mVorC = random.randint(0, 1)
            if mVorC == 0:
                mC = random.choice(laterC)
                eC = random.choice(laterVC)
                return fC+lV+mC+eC
            else:
                mV = random.choice(laterVC)
                eV = random.choice(finalV)
                return fC+lV+mV+eV
        else:
            mV = random.choice(laterVC)
            mC = random.choice(laterC)
            oV = random.choice(laterVC)
            eVorC = random.randint(0, 1)
            if eVorC == 0:
                eV = random.choice(finalV)
                return fC+lV+mV+mC+oV+eV
            else:
                eC = random.choice(laterVC)
                return fC+lV+mV+mC+oV+eC

print namer()
