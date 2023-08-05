from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/", response_class=Response)
async def read_root(request: Request):
    # Your HTML content goes here

	html_content = '''<html><head><title>Welcome</title></head><body><h1>Welcome</h1><p>Hello World</p><ul><li><a href="localhost:8080/sourceWiki">click 1</a></li> <li><a href="https://www.example.com">click 2</a></li>        <li><a href="https://www.example.com/link3">link 3</a></li><li><a href="http://127.0.0.1:8000/items/100">link 4</a></li></ul></body></html>'''
	return html_content


@app.get("/items/{item_id}", response_model=dict)
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
