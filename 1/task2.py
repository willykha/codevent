# hacky
def main():
    with open("task1.txt") as file:
        numbers = []
        for line in file:
            numbers.append(int(line))
            
        find2020(numbers)

def find2020(nums):
    for number in nums:
        for number2 in nums:
            for number3 in nums:
                if (number+number2+number3 == 2020):
                    print(number*number2*number3)

if __name__ == "__main__":
    main()