from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    Error_Msg:str
    Error_Code:int
    Status:bool
    Result:str

class PostBody(BaseModel):
    Name:str
    description: str = None #表示可空

app = FastAPI()


@app.get("/")
async def root():
    """
    默认请求
    :return:hello world
    """
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    带参数/可选参数查询
    :param item_id:
    :param q:
    :return:
    """
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def put(item:Item):
    """
    带Model查询
    :param item:
    :return:
    """
    return {"Error_Msg":item.Error_Msg,"Error_Code":int(item.Error_Code),"Result":item.Result,"Status":item.Status}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int=10,param:Optional[str] = None):
    """
    分页信息查询
    :param skip:
    :param limit: Optional[int] = None表示参数可能为None
    :return:
    """
    if limit <0 or limit==0:
        limit=10
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    return fake_items_db[skip : skip + limit]



@app.post("/post")
async def post(request:PostBody):
    """
    POST请求示例
    :param request:
    :return:
    """
    if not request.description.strip():
        request.description="当前description为空"
    return {"Error_Msg":None,"Error_Code":0,"Result":{"description":request.description,"Name":request.Name},"Status":True}

@app.get("/paramVerify")
def paramVerify(q: str = Query(None, min_length=3, max_length=50)):
    """
    参数校验
    :param item_id:
    :param q:
    :return:
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results