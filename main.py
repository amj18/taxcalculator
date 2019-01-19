from countryTaxClasses import UKTax

if __name__ == "__main__":
    ukTaxCalc = UKTax(25000, 162, 892, 0.12, 0.02, 11859, 0.2, 0.4, 0.45, 34500, 150000, 0.09, 18330)
    print(ukTaxCalc.national_insurance_rate_uk())
