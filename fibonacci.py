result = []
def fibonacci(n: int) -> int:
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        # result.append(0)
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        # result.append(1)
        return 1

    else:
        x = fibonacci(n-1) + fibonacci(n-2)
        # result.append(x)
        return x

if __name__ == "__main__":
    res = fibonacci(5)
    # print(result)
    print(res)

# # 3
# (3-1) + (3-2) = (2) + (1)

#     # 2
#     (2-1) + (2-2) = (1) + (0)
#     (1) + (0) = (1) + (1)
#     (1) + (0) = (1) + (0)
#     (1) = (1)

#         # 1
#         (1-1) + (1-2) = (1) + (0)
#         (1) + (0) = (1) + (1)
#         (1) + (0) = (1) + (0)
#         (1) = (1)