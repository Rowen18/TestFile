import webbrowser
browser = input("Type the name of your preferred browser:")
URL = input("Type the URL of the website you want to go to:")
webbrowser.get(browser + "%s")
webbrowser.open(URL, new=2, autoraise=True)
