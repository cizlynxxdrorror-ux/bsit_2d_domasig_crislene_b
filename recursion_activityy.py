


def sum_array(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_array(numbers[1:])


def largest_number(numbers):
    if len(numbers) == 0:
        raise ValueError("Array must not be empty")

    if len(numbers) == 1:
        return numbers[0]

    largest_rest = largest_number(numbers[1:])

    if numbers[0] > largest_rest:
        return numbers[0]
    else:
        return largest_rest



def count_number(numbers, target):
    if len(numbers) == 0:
        return 0

    if numbers[0] == target:
        return 1 + count_number(numbers[1:], target)
    else:
        return count_number(numbers[1:], target)



print("Sum:", sum_array([2, 4, 6, 8]))
print("Largest:", largest_number([5, 12, 3, 20, 8]))
print("Count:", count_number([2, 5, 2, 8, 2, 10], 2))
