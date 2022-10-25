try:
    with open('text.txt1', 'r') as reader:
        print(reader.read())
except Exception as e:
    print(e)

finally:
    print("cleaning source")
