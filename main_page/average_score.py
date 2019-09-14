def average():
    first_grade = float(input("please, enter your next grade"))
    second_grade = float(input("please, enter your next grade"))
    third_grade = float(input("please, enter your next grade"))
    average_= first_grade + second_grade + third_grade
    total = average_/3
    return total

if __name__ == '__main__':
    average()
