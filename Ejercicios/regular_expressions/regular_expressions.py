import re

def main():
    text: str = """In a hidden valley, where the mist never quite lifts and the trees shimmer 
with an ethereal glow, there exists a rare phenomenon: the Song of the Moon. Once every 
century, the moon rises over the valley at midnight, casting its silver light onto the 
forest floor. In that moment, the trees themselves begin to hum, their leaves vibrating 
in harmony with the pulse of the earth. The sound is a melody like no other—so ancient 
and soothing that even the most restless souls find peace. Legend has it that if you 
listen closely, you can hear whispers from forgotten times, secrets passed down through 
generations, carried by the moon’s light. Those lucky enough to witness the Song are 
said to be touched by a bit of magic, seeing the world through new eyes forevermore."""

    pattern = re.compile("the")
    res = pattern.findall(text)
    print (res)


if __name__ == '__main__':
    main()