def nbMonths(old, new, saving, percent):
    month = 0
    while old - new + saving * month < 0:
        month += 1
        devalue = (100.0 - percent - 0.5 * (month / 2)) / 100.0
        old *= devalue
        new *= devalue
    return [month, round(old - new + saving * month)]
    
    
OR


def nbMonths(oldCarPrice, newCarPrice, saving, loss):
    months = 0
    budget = oldCarPrice
    
    while budget < newCarPrice:
        months += 1
        if months % 2 == 0:
            loss += 0.5
        
        oldCarPrice *= (100 - loss) / 100
        newCarPrice *= (100 - loss) / 100
        budget = saving * months + oldCarPrice
    
    return [months, round(budget - newCarPrice)]
    
    
    
    
OR



def nbMonths(old, new, saving, percent):
    diff, m = old - new, 0
    while diff + saving * m < 0:
        m += 1
        diff *= (100.0 - percent - 0.5 * (m / 2)) / 100.0
    return [m, round(diff + saving * m)]
