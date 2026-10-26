def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return n / 2.54

def ft_to_cm(n):
    return n * 30.48

def inch_to_cm(n):
    return n * 2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'178cm = {cm_to_inch(178)}inch')
    print(f'7ft = {ft_to_cm(7)}cm')
    print(f'8inch = {inch_to_cm(8)}cm')