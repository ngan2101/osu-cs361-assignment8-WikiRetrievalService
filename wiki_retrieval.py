import wikipedia

def get_random_page_content():
    page_title = wikipedia.random()
    page_content = wikipedia.page(page_title).content
    return page_content

