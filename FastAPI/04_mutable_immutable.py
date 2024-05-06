# str is immutable

a = "corey"
print(a)
print(f"Address of a is {id(a)}")
a = "john"
print(a)
print(f"Address of a is {id(a)}")


a[0] = "x"  # because immutable


"""
        immutable does not mean that , `a` can not be assigned again.
        Its not modifying the previous string object its creating new one.
        
        Memory address does not changes in case of mutable. because values are replaced inplace
"""
