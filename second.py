def maxCost(cost, labels, dailyCount):
    total_cost = 0
    day_cost = 0
    legal_count = 0
    max_day_cost = 0
    
    for i in range(len(cost)):
        day_cost += cost[i]
        if labels[i] == "legal":
            legal_count += 1
            
        if legal_count == dailyCount:
            max_day_cost = max(max_day_cost, day_cost)
            day_cost = 0
            legal_count = 0
            
    return max_day_cost