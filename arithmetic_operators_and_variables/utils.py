
def mass_and_charge(neutrons, electrons, protons):
    mass = neutrons + protons
    charge = protons - electrons
    return [mass, charge]

def neutrons_and_electrons(charge, mass, protons):
    neutrons = mass - protons
    electrons = protons - charge
    return [neutrons, electrons]

def neutrons_and_protons(charge, mass):
    protons = mass - charge
    neutrons = mass - protons
    return [neutrons, protons]

def protons_and_electrons(charge, mass, neutrons):
    protons = mass - neutrons
    electrons = protons - charge
    return [protons, electrons]

def mass_and_electrons(charge, neutrons, protons):
    mass = neutrons + protons
    electrons = protons - charge
    return [mass, electrons]

def protons_and_mass(charge, neutrons):
    protons = neutrons + charge
    mass = neutrons + protons
    return [protons, mass]

def neutrons_and_charge(mass, electrons, protons):
    neutrons = mass - protons
    charge = protons - electrons
    return [neutrons, charge]

def protons_and_charge(mass, neutrons, electrons):
    protons = mass - neutrons
    charge = protons - electrons
    return [protons, charge]
