try:
    f = open("sample.txt", "w")
    f.write("Hello, Python!")
    print("File written successfully.")
except Exception as e:
    print("Error occurred:", e)
finally:
    f.close()
    print("File closed.")