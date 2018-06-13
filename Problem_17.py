def main():
    ten = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen',
           'fourteen','fifteen']
    tens = ['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    longstring = ''
    for number in range(1, 99+1):
        if number < 16:
            longstring += ten[number]
        elif number < 20:
            longstring += (ten[int(str(number)[1])] + 'teen')
        elif number < 100:
            longstring += (tens[int(str(number)[0])] + ten[int(str(number)[1])])
        elif number < 1000:
            longstring += (ten[int(str(number)[0])] + 'hundred and ' + tens[int(str(number)[1]) + ten[int(str(number)[2]])

    print longstring
    print len(longstring)



if __name__ == '__main__':
    main()
