#vijay went to hotel for dinner his bill is 2500,gst applicable is 5%
#hotel manager has given him 5% dicount,how much vijay has to pay

bill = 2500
after_discount = bill-(bill*0.05)
gst_applied = after_discount * 0.05
final_pay = after_discount + gst_applied
print(final_pay)
