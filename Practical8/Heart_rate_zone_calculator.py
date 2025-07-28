def heart_rate_zone(age, bpm):
    max_hr = 220 - age
    if bpm > max_hr:
        return "Error: Heart rate exceeds maximum safe value."
    if bpm < 0.5 * max_hr:
        return "Error: Heart rate too low for exercise zone."
    
    percent = bpm / max_hr
    if percent < 0.6:
        return (1, "Very light exercise")
    elif percent < 0.7:
        return (2, "Light exercise")
    elif percent < 0.8:
        return (3, "Moderate exercise")
    elif percent < 0.9:
        return (4, "Hard exercise")
    else:
        return (5, "Maximum")
print(heart_rate_zone(20, 160))
# ➜ (4, 'Hard exercise')
