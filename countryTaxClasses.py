class UKTax():
    def __init__(self, salary, ni_a, ni_b, ni_p1, ni_p2, personalAllowance, basicRate, higherRate, additionalRate, basicUL, higherUL, studentLoanRate, studentLoanLL):
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

        def national_insurance_rate_uk(self):
            weeklySalary = self.salary/52.0
            if weeklySalary <= self.ni_a:
                return 0.0
            elif weeklySalary > self.ni_a and weeklySalary <= self.ni_b:
                return (self.ni_p1*(weeklySalary-ni_a))
            elif weeklySalary > ni_b:
                return (ni_p1*(ni_b-ni_a))+(ni_p2*(weeklySalary-ni_b))
