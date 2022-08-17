import basic

# Running an infinite loop to take input
while True:
    text = input('toy > ')
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)