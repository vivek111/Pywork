"""
Document here

>>> shorten("The road to hell is here")
'The road to ...'
>>> shorten("All roads lead nowhere", length = 10)
'All roa...'
>>> shorten(length = 8, text ="What goes up")
'What ...'
>>> shorten("Watched Pot never boils", 9, "*")
'Watched *'

"""
def shorten(text, length=15, indicator="..."):
    if len(text) > length:
        text = text[:length -len(indicator)] + indicator
    return text


print(shorten("The road to hell is here"))
print(shorten("All roads lead nowhere", length = 10))
print(shorten(length = 8, text ="Whats goes up"))
print(shorten("Watched Pot never boils", 9, "*"))




