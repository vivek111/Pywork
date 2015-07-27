import TextUtil

print("Docstring for module")
docstr=TextUtil.is_balanced.__doc__#To fetch the documentation
print(docstr)
text="	To 	be 			or  Not tobe"
print(text)
text=TextUtil.simplify(text)
print(text)
