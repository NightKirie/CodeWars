def narcissistic( value ):
    return value == sum(i ** len(str(value)) for i in [int(x) for x in str(value)])
