# Mama Guard - Simple AI Risk Detection Model

def health_risk(bp, heart_rate, temperature):
    if bp > 140 or heart_rate > 100 or temperature > 38:
        return "⚠️ High Risk - Immediate attention needed"
    elif bp > 120:
        return "⚠️ Moderate Risk - Monitor closely"
    else:
        return "✅ Normal"

# Example test
print(health_risk(150, 110, 37))
