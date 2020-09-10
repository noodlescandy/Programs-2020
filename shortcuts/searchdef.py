import webbrowser, pyperclip

query = pyperclip.paste()
search = "https://www.duckduckgo.com/?q=" + query + "+biology+definition"

webbrowser.open_new_tab(search)