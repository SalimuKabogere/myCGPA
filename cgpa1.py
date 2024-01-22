class Calculator:
    # addition
    def addition(x,y):
        """
        this peforms the basic addition of two numbers
        x and y
        """
        return x+y
    
    # subtraction
    def subtraction(x,y):
        return x-y
    
    # multiplication
    def multiplication(x,y):
        return x*y
    
    # division
    def division(x,y):
        if y!=0:
            return x/y
        else:
            print("cannot divide by 0")

class CGPA(Calculator):
    def calculate_cgpa(self,subjects):
        total_credit_points=0
        total_credits=0
        for credits, grade in subjects:
            credit_points=Calculator.multiplication(credits,grade)
            total_credit_points=Calculator.addition(total_credit_points,credit_points)
            total_credits=Calculator.addition(total_credits,credits)
        gpa=Calculator.division(total_credit_points,total_credits)
        return gpa
        # example test
subjects_data=[
        (3,5),
        (3,5),
        (3,5.0),
        (4,4.0),
        (4,5),
        (4,5)
    ]
cgpa1=CGPA().calculate_cgpa(subjects_data)
rounded=round(cgpa1,4)
print("the cgpa is:\n",rounded)