"""
File: taxformwithgui.py
Project 8.6
A GUI-based tax calculator.

Computes and prints the total tax, given the income and
number of dependents (inputs), and a standard deduction of
$10,000, an exemption amount of $3,000, and tax rates of
20% for Single
15% for Married
10% for Divorced
"""

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator")

        # Label and field for the income
        self.addLabel(text="Income", row=0, column=0)
        self.incomeField = self.addFloatField(value = 0.0, row=0, column=1)


        # Label and field for the number of dependents
        self.addLabel(text="Dependents", row=1, column=0)
        self.depField= self.addIntegerField(value=0, row=1, column=1)


        self.statusGroup = self.addRadiobuttonGroup(row = 0, column = 2,
                                              columnspan =1,
                                                            )

        # Radio buttons for filing status
        defaultRB =self.statusGroup.addRadiobutton("single")
        self.statusGroup.addRadiobutton("married")
        self.statusGroup.addRadiobutton("divorced")

        # Select one of the buttons in the group
        defaultRB = self.statusGroup.setSelectedButton(defaultRB)

        # Button group (self.statusGroup)
        # Option for single (self.single)
        # Option for married (self.married)
        # Option for divorced (self.divorced)
 
        self.addButton(text="Compute",row=2, column=0, 
        columnspan=2, command= self.computeTax)


        self.addLabel(text="Total tax",row=4, column=0)
        self.taxField=self.addFloatField(value=0.0, row=4, column=1, precision=2)


    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field (taxField)."""

        income= self.incomeField.getNumber()
        numDependents= self.depField.getNumber()

        status = self.statusGroup.getSelectedButton()
        rate = 0;
        if(status==self.statusGroup("married")):
            rate=15
        elif(status == "divorced"):
            rate=10
        else:
            rate=20

        exemptionAmount = (numDependents*3000)


        tax =(income - (10000+exemptionAmount)) * rate

        self.taxField.setNumber(tax)

        
        
def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()

