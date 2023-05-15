# fizzbuzz game with python but we can add more rules

def fizzbuzz(number):
    string = ""
    if number % 3 == 0:
        string += "Fizz"
    if number % 5 == 0:
        string += "Buzz"
    if number % 7 == 0:
        string += "Bang"
    if string == "":
        string = str(number)
    return string
    
def main():
    for number in range(1, 101):
        print(fizzbuzz(number))

if __name__ == "__main__":
    main()
