#Section 1: Basic String Manipulation
#1. Student Name Formatter
name = "sAkEtH kAlLePu"
print(name.title())


#2. Customer Email Cleanup
email = " Saketh.KALLEPU@GMAIL.COM "
print(email.strip().lower())


#3. Product Code Replacement
product_code = "OLD-101-OLD-202"
print(product_code.replace("OLD", "NEW"))


#4. Username Generator
first_name = "SAKETH"
year = 2027
print(first_name.lower() + "_" + str(year))


#5. Sentence Character Count
sentence = "Python makes coding easy"
print(len(sentence))


#Section 2: Indexing and Slicing
#6. Employee ID Extraction
employee_id = "EMP582741"
print(employee_id[3:])


#7. Mask a Bank Account Number
account_number = "123456789012"
print("*" * 8 + account_number[-4:])


#8. Alternating Character Extraction
text = "CODEGNANPYTHON"
print(text[::2])


#9. Reverse a Product Serial Number
serial_number = "PYTHON123"
print(serial_number[::-1])


#10. Extract a File Extension
filename = "student_report.pdf"
print(filename[-3:])


#Section 3: Searching, Splitting, and Joining
#11. Search for a Course Name
description = "Python is easy. I love PYTHON. Learn python today."
print(description.lower().count("python"))


#12. Convert a Sentence into Words
sentence = "Learn Python Full Stack Development"
print(sentence.split())


#13. Generate a Formatted Address
house = "12-4"
street = "MG Road"
city = "Vijayawada"
state = "Andhra Pradesh"
print(", ".join([house, street, city, state]))


#14. Count Words in a Message
message = "Your application has been successfully submitted"
print(len(message.split()))


#15. Validate a Coupon Code
coupon_code = "CODEGNAN"
print(coupon_code.isalpha())


#Additional test:

coupon_code = "CODEGNAN123"
print(coupon_code.isalpha())

