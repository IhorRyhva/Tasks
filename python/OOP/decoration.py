import webbrowser

def validator(func):
    def wrapper(url):
        if "." in url:
            print("Посилання праильне")
            func(url)
        else:
            print("Посилання непраильне")
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)


open_url('https://itproger.com/ua/course/python/20')