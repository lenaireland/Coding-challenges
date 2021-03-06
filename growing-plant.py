def growingPlant(upSpeed, downSpeed, desiredHeight):
    """Each day a plant is growing by upSpeed meters. Each night that plant's 
    height decreases by downSpeed meters due to the lack of sun heat. Initially,
    plant is 0 meters tall. We plant the seed at the beginning of a day. We want
    to know when the height of the plant will reach a certain level."""

    height = 0
    days = 0
    
    
    while True:
        days += 1
        height += upSpeed
        
        if height >= desiredHeight:
            return days
        else:
            height -= downSpeed