def eligilbe_Placement_attendence_percent(attendence_percent: float) -> str:
    if attendence_percent >= 75:
        return "Eligible for Placement"
    else:
        return "Not Eligible for Placement"
      
attendence_percent = float(input("Enter your attendence percentage: "))
result = eligilbe_Placement_attendence_percent(attendence_percent)
print(result)