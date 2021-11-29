# Purpose is to create a program for harry's car lot
# Author, Noah Gosse
# Date, Oct-27-2021  Last modified Nov-12-2021, Finished the display and fixed other errors with calculations for outputs

# Modules/Functions

import datetime

# Constants

TAX_RATE = .15
STANDARD_RATE = 75.00
LUXTAX_RATE = .016
TRANFEE_RATE = .01
FINANCING_FEE_RATE = 39.99

# User Inputs and Validations

while True:

    while True:
        CustFirst = input("Enter the customer first name (Must be entered): ")

        if CustFirst.title() == "":
            print("Name cannot be blank, please enter a name")
        else:
            break

    while True:
        CustLast = input("Enter the customer last name (Must be entered): ")

        if CustLast.title() == "":
            print("Name cannot be blank, please enter a name")
        else:
            break
    Address = input("Enter customer address: ")
    City = input("Enter customer city: ")
    Prov = input("Enter customer province: ")
    PostCode = input("Enter customer postal code: ")

    while True:
        Phone = input("Enter the customer phone number (10 digits): ")

        if len(Phone) !=10:
            print("Invalid phone number, must contain 10 digits")
        else:
            break

    while True:
        try:
            PurDate = input("Enter the date of the purchase (YYYY-MM-DD): ")
            PurDate = datetime.datetime.strptime(PurDate, "%Y-%m-%d")
        except:
             print("Invalid date, make sure to enter in the correct format")
        else:
            break

    while True:
        PlatNum = input("Enter the plate number (XXX999): ")

        if PlatNum.capitalize == "":
            print("Plate number cannot be blank, please enter a plate number")
        else:
            break

    CarYear = input("Enter the year of the car: ")
    CarModel = input("Enter the car make and model: ")

    while True:
        try:
            SellPrice = float(input("Enter the selling price (Cannot exceed $50000): "))
        except ValueError:
            print("Invalid entry, make sure you entered the correct amount")
        else:
            if SellPrice > 50000 or SellPrice == "":
                print("Invalid price, cannot be blank and cannot exceed $50000")
            else:
                break

    while True:
        try:
            TradeAmt = float(input("Enter the trade in amount (Cannot exceed selling price): "))
        except ValueError:
            print("Invalid price, make sure you entered the correct amount")
        else:
            if TradeAmt > SellPrice:
                print("Trading amount cannot exceed selling price, please re-enter")
            else:
                break

    SalePerName = input("Enter the salesperson name: ")
    CredCardNum = input("Enter the credit card number: ")
    ExpDate = input("Enter the expiry date: ")

# Calculations

    AfterTrade = SellPrice - TradeAmt
    HST = SellPrice * TAX_RATE

    if SellPrice <= 5000:
        LicenceFee = SellPrice + STANDARD_RATE
    else:
        LicenceFee = SellPrice + 165.00

    TransFee = SellPrice * TRANFEE_RATE

    if SellPrice > 20000:
        LicenceFee = SellPrice * LUXTAX_RATE

    TotalSalePrice = AfterTrade + TAX_RATE + LicenceFee + TransFee
    Years = 0

    TotalPrice = TotalSalePrice + FINANCING_FEE_RATE

# Outputs

    print()
    print("# Years    # Payments    Financing Fee    Total Price  Monthly Payment")
    print("----------------------------------------------------------------------")
    for years in range(1, 5):
        NumPay = years * 12
        FinFee = 39.99 * years
        TotalCost = TotalPrice + FinFee
        MonPay = TotalPrice / NumPay
        FinFeeStr = "${:,.2f}".format(FinFee)
        FinFeePad = "{:>10}".format(FinFeeStr)
        TotalCostStr = "${:,.2f}".format(TotalCost)
        TotalCostPad = "{:>10}".format(TotalCostStr)
        MonPayStr = "${:,.2f}".format(MonPay)
        MonPayPad = "{:>10}".format(MonPayStr)

        print(" "*3, years," "*9, NumPay,    "       {}       {}      {}".format(FinFeePad, TotalCostPad, MonPayPad))


    PurchaseDate = datetime.date.today()
    print()
    print("Purchase Date: ", PurchaseDate)

    PayDate = PurchaseDate + datetime.timedelta(days=30)
    print("First Payment Date: ", PayDate)
    print()

# Input for payment method

    while True:
        try:
            PayMethod = int(input("Enter the payment method you would like to use (must be between 1-4): "))
        except ValueError:
            print("Invalid entry, please make sure your number is between 1 and 4")
        else:
            if PayMethod < 1 or PayMethod > 4:
                print("Invalid entry, please make sure your number is between 1 and 4")
            else:
                break

    NumPay = PayMethod * 12
    FinFee = 39.99 * PayMethod
    TotalCost = TotalPrice + FinFee
    MonPay = TotalPrice / NumPay

    SellPriceStr = "${:,.2f}".format(SellPrice)
    SellPricePad = "{:>10}".format(SellPriceStr)

    TradeAmtStr = "${:,.2f}".format(TradeAmt)
    TradeAmtPad = "{:>10}".format(TradeAmtStr)

    AfterTradeStr = "${:,.2f}".format(AfterTrade)
    AfterTradePad = "{:>10}".format(AfterTradeStr)

    HSTStr = "${:,.2f}".format(HST)
    HSTPad = "{:>10}".format(HSTStr)

    LicenceFeeStr = "${:,.2f}".format(LicenceFee)
    LicenceFeePad = "{:>10}".format(LicenceFeeStr)

    TransFeeStr = "${:,.2f}".format(TransFee)
    TransFeePad = "{:>10}".format(TransFeeStr)

    TotalSalePriceStr = "${:,.2f}".format(TotalSalePrice)
    TotalSalePricePad = "{:>10}".format(TotalSalePriceStr)

    MonPayStr = "${:,.2f}".format(MonPay)
    MonPayPad = "{:>10}".format(MonPayStr)

# Final Outputs

    print()
    print(" "*9, "Honest Harry Car Sales")
    print(" "*8, "Used Car Sale and Receipt")
    print()
    print("Invoice Date: ", PurDate.strftime("%b %d, %Y"))
    print("Receipt No: ", CustFirst[0], CustLast[0], PlatNum[3:7], Phone[6:11])
    print("Sold To: ")
    print(" "*6, CustFirst[0] + ".  ", CustLast)
    print(" "*6, City, Prov, PostCode)
    print()
    print("Car details: ")
    print(" "*6, CarYear, CarModel)
    print()
    print("Sale Price:                  {}".format(SellPricePad))
    print("Trade Allowance:             {}".format(TradeAmtPad))
    print("Price After Trade:           {}".format(AfterTradePad))
    print(" "*28, "----------")
    print("HST:                         {}".format(HSTPad))
    print("License Fee:                 {}".format(LicenceFeePad))
    print("Transfer Fee:                {}".format(TransFeePad))
    print(" "*28, "----------")
    print("Total Sales Cost:            {}".format(TotalSalePricePad))
    print()
    print("Terms: ", PayMethod, " "*9, "Total Payments: ", NumPay)
    print("Monthly Payment:             {}".format(MonPayPad))
    print()
    print(" "*4, "Honest Harry Car Sales")
    print("Best used cars at the best price!")

    Continue = input("Would you like to enter another sale? (Y)yes (N)no: ")
    if Continue.upper() == "N":
        break
