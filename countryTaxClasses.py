class UKTax():
    def __init__(self, salary, ni_a, ni_b, ni_p1, ni_p2, personalAllowance, basicRate, higherRate, additionalRate, basicUL, higherUL, studentLoanRate, studentLoanLL, studentLoan):
        """
        Constructor for UK tax variables.
        """
        self.salary = salary
        self.ni_a = ni_a
        self.ni_b = ni_b
        self.ni_p1 = ni_p1
        self.ni_p2 = ni_p2
        self.personalAllowance = personalAllowance
        self.basicRate = basicRate
        self.higherRate = higherRate
        self.additionalRate = additionalRate
        self.basicUL = basicUL
        self.higherUL = higherUL
        self.studentLoanRate = studentLoanRate
        self.studentLoanLL = studentLoanLL
        self.studentLoan = studentLoan  

    def national_insurance_rate_uk(self):
        """
        Calculates UK National Insurance as of 2018/2019
        """
        weeklySalary = self.salary/52.0
        if weeklySalary <= self.ni_a:
            return 0.0
        elif weeklySalary > self.ni_a and weeklySalary <= self.ni_b:
            return (self.ni_p1*(weeklySalary-self.ni_a))
        elif weeklySalary > self.ni_b:
            return (self.ni_p1*(self.ni_b-self.ni_a))+(self.ni_p2*(weeklySalary-self.ni_b))

    def salary_after_tax_uk(self):
        """
        Calculates Salary after tax with/without Student Loan contributions
        """
        taxableIncome = self.salary-self.personalAllowance
        ni = national_insurance_rate_uk()*52.0  
        threshold = self.salary - self.studentLoanLL
        sl = threshold*self.studentLoanRate
        if salary <= self.personalAllowance: # if salary is below personal allowance
            return self.salary  
        elif taxableIncome <= self.basicUL: # salary at basic rate tax
            if self.studentLoan==True and self.salary>self.studentLoanLL: # with student loan
                totalTaxable = taxableIncome*self.basicRate
                totalDeductions = totalTaxable + sl + ni    
                final = self.salary - totalDeductions
                return final    
            else: # without student loan
                totalTaxable = taxableIncome*self.basicRate
                totalDeductions = totalTaxable + ni 
                final = self.salary - totalDeductions
                return final   
        
        # Tax up to upper limit of basic rate
        elif taxableIncome > self.personalAllowance and taxableIncome <= self.basicUL:
            if self.studentLoan==True and self.salary>self.studentLoanLL:
                totalTaxable = taxableIncome*self.basicRate
                totalDeductions = totalTaxable+sl+ni
                final = salary-totalDeductions
                return final
            else:
                totalTaxable = taxableIncome*self.basicRate
                totalDeductions = totalTaxable+ni
                final = salary-totalDeductions
                return final

