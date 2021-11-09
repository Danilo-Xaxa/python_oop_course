class MyEditorialBook:
    
    has_cover = True
    editorial_code = 39012
    
    def __init__(self, title, num_pages, published):
        self.title = title
        self.num_pages = num_pages
        self.published = published
        
cover = True
code = 39012

# Add your variables below this line
MyEditorialBook.has_cover = cover
MyEditorialBook.editorial_code = code
