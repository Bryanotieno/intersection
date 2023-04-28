# Intersection calculation.

import math as m  # Import math library used in join computation


# (N1,E1) and (N2,E2) are coordinates of instrument station and foresight stations respectively.
def main():
    NA = float(input("Enter Northings of A:"))
    EA = float(input("Enter Eastings of A:"))
    NB = float(input("Enter Northings of B:"))
    EB = float(input("Enter Eastings of B:"))

    BEARING_AC = float(input('User input Bearing AC:'))
    BEARING_BC = float(input('User input Bearing BC:'))

    a = ((NB-NA)*(m.radians(m.tan(BEARING_BC))))-(EB-EA)
    b = (m.radians(m.tan(BEARING_BC))) - (m.radians(m.tan(BEARING_AC)))
    print(a, b)
    NC = NA + (a / b)

    EC = EA + (NC-NA)*m.radians(m.tan(BEARING_AC))

    print('\nnorthing of C equals:', NC)
    print('\neasting of C equals:', EC)

    Repeat = input("would you like to continue?:")

    if Repeat == "Yes":
        main()
    elif Repeat == "No":
        exit()


main()