def angle(h, m):

    if h > 12:
        h = 0
    if m > 60:
        m = 0

    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m

    angle = abs(hour_angle - minute_angle)
    angle = min(angle, 360-angle)

    return angle

print(angle(1, 30))
