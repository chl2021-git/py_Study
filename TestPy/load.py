import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def printStatistics(capitals, interests, total_payment, months):
    print("总本金：" + str(np.sum(capitals)))
    print("总利息：" + str(np.sum(interests)))
    print("总利息/总本金" + str(np.sum(interests)/np.sum(capitals)))
    print("首月还款 %.2f 末月还款： %.2f" % (total_payment[0], total_payment[months - 1]))

def drawDiagram(months, fn, *args, **kwargs):
    capitals, interests, total_payment = fn(months, *args, **kwargs)
    printStatistics(capitals, interests, total_payment, months)
    month_array = np.arange(1, months + 1, 1)
    height = interests
    plt.bar(month_array, capitals, width=0.2, align='center', color='red')
    plt.bar(month_array, interests, width=0.2, align='center', color='blue', bottom=capitals)
    plt.show()

def normalPaid(months, principal, rate, capitalAveraged):
    month_rate = rate / 12
    monthly_capital = principal / months
    monthly_payment = principal * month_rate * (1 + month_rate) ** months / ((1 + month_rate) ** months - 1)
    interests = [0] * months
    capitals = [0] * months
    left_principal = [0] * months
    left_principal[0] = principal
    total_payment = [0] * months
    for i in range(0, months):
        interests[i] = left_principal[i] * month_rate
        if capitalAveraged:
            capitals[i] = monthly_capital
            total_payment[i] = monthly_capital + interests[i]
        else:
            total_payment[i] = monthly_payment
            capitals[i] = total_payment[i] - interests[i]
        if i + 1 < months:
            left_principal[i + 1] = left_principal[i] - capitals[i]
    return capitals, interests, total_payment

def getFirstPaid(months, principal, rate, capitalAveraged):
    month_rate = rate / 12
    monthly_capital = principal / months
    monthly_payment = principal * month_rate * (1 + month_rate) ** months / ((1 + month_rate) ** months - 1)
    interests1 = principal * month_rate
    if capitalAveraged:
        return monthly_capital + interests1, monthly_capital
    else:
        return monthly_payment, monthly_payment - interests1
def getLeftMonths(leftMonthsMax, capitalPaidMax, paidMax, leftPrincipal, rate, capitalAveraged):
    lastPaid, lastCapitalPaid, lastMonths = 0, 0, 0
    for i in range(leftMonthsMax, 1, -1):
        paid, capitalPaid = getFirstPaid(i, leftPrincipal, rate, capitalAveraged)
        if paid > paidMax or (capitalAveraged and capitalPaid > capitalPaidMax):
            return lastMonths, lastPaid, lastCapitalPaid
        else:
            lastPaid, lastCapitalPaid, lastMonths = paid, capitalPaid, i
#总还款月数，本金，利率，等额本金or等额本息，提起还款月数
def extraPaidWithFixedPaid(months, principal, rate,
                           capitalAveraged, extraPaidList: list):
    capitals, interests, total_payment = normalPaid(
        months, principal, rate, capitalAveraged)
    extraPaidList.sort(key=lambda x: x[0])
    originCapital, originInterests, originTotal = capitals.copy(), interests.copy(), total_payment.copy()
    left_principal = [0] * months
    left_principal[0] = principal
    for x in range(0, months):
        if x < months - 1:
            left_principal[x + 1] = left_principal[x] - capitals[x]

    def normalPaidOffset(left_months, principal, rate,
                         capitalAveraged, offset, left_months2):
        month_rate = rate / 12
        monthly_capital = left_principal[offset] / left_months
        monthly_payment = left_principal[offset] * month_rate * (1 + month_rate) ** left_months / ((1 + month_rate) ** left_months - 1)
        for i in range(0, left_months):
            interests[offset + i] = left_principal[offset + i] * month_rate
            if capitalAveraged:
                capitals[offset + i] = monthly_capital
                total_payment[offset + i] = monthly_capital + interests[offset + i]
            else:
                total_payment[offset + i] = monthly_payment
                capitals[offset + i] = total_payment[offset + i] - interests[offset + i]
            if i == 0:
                print("次月还款 %.2f" % total_payment[offset + i])
            if offset + i + 1 < months:
                left_principal[offset + i + 1] = left_principal[offset + i] - capitals[offset + i]
        for i in range(left_months, left_months2):
            interests[offset + i] = 0
            capitals[offset + i] = 0
            total_payment[offset + i] = 0
        return
    realMonth = months
    for x, y in extraPaidList:
        capitalParam = capitals[x]
        capitals[x] = capitals[x] + y
        left_principal[x + 1] = left_principal[x] - capitals[x]
        total_payment[x] = capitals[x] + interests[x]
        maxMonth, maxPaid, maxPaidCapital = getLeftMonths(months - x - 1, capitalParam, total_payment[x - 1], left_principal[x + 1], rate, capitalAveraged)
        normalPaidOffset(maxMonth, left_principal[x + 1], rate, capitalAveraged, x + 1, months - x - 1)
        realMonth = x + 1 + maxMonth
        print("当月需还 %.2f 剩余本金 %.2f 下月需还：%.2f  原本剩余账期：%d,当前剩余账期：%d, 账期缩短：%d" %(total_payment[x], left_principal[x + 1],total_payment[x + 1], months - x - 1,maxMonth, months - x - 1 - maxMonth))
    printStatistics(originCapital, originInterests, originTotal, months)
    print("")
    printStatistics(capitals, interests, total_payment, realMonth)
    print("节省利息 %.2f" % (np.sum(originInterests) - np.sum(interests)))
    return capitals, interests, total_payment, originTotal, originInterests
def drawDiagramExtraPaid(months, capitals, interests, originalTotal, originalInterests, showOriginTotal=True):
    month_array = np.arange(1, months + 1, 1)
    capital_with_origin_interest = [0] * months
    height = interests
    for x in range(1, months):
        capital_with_origin_interest[x] = capitals[x] + originalInterests[x]
    l1 = plt.bar(month_array, originalTotal if showOriginTotal else capital_with_origin_interest, width=0.2, align='center', color='yellow')
    l2 = plt.bar(month_array, capitals, width=0.2, align='center', color='red')
    l3 = plt.bar(month_array, interests, width=0.2, align='center', color='blue', bottom=capitals)
    # plt.legend(handles = [l1, l2,l3], labels = ['每月少还' if showOriginTotal else '节省利息', '本金','利息'], loc = 'best',fontsize=20)
    plt.ylim(0, (capitals[0]+interests[0])*1.1)
    plt.show()

def drawTableExtraPaid(months, capitals, interests, total_payment, originalTotal, originalInterests):
    paid_capital = [0] * months
    paid_interests = [0] * months
    saved_money = [0] * months
    paid_capital[0] = capitals[0]
    paid_interests[0] = interests[0]
    for x in range(1, months):
        paid_capital[x] = paid_capital[x - 1] + capitals[x]
        paid_interests[x] = paid_interests[x - 1] + interests[x]
        saved_money[x] = saved_money[x - 1] + (originalInterests[x] - interests[x] )
    origin = pd.DataFrame([total_payment, capitals, interests, paid_capital, paid_interests,saved_money])
    return pd.DataFrame(origin.values.T, columns=['还款额','还款本金','还款利息','已还本金','已还利息','累计节省'], index=np.arange(1, months + 1))

a, b, c, d, e = extraPaidWithFixedPaid( 178, 667707.08, 0.0479, False, [(0, 100000)])
drawDiagramExtraPaid(178, a, b, d, e)
drawTableExtraPaid(178, a, b, c, d, e)[10:50]