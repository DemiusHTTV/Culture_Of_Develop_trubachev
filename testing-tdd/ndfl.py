def calculate_tax(income):
    if income<2400000:
        return income *0.13
    elif income <5_000_000:
        return(2_400_00*0.13 +(income -2_400_00)*0.15)
    elif income <20_000_000:
        return(2_400_000 *0.13 +2_600_00*0.15+(income-5_000_000)*0.15)