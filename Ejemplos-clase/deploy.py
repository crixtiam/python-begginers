from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pickle
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Price(BaseModel):
    OverallQual: str
    GrLivArea: str
    GarageCars: str
    GarageArea   : str
    TotalBsmtSF  : str
    stFlrSF     : str
    FullBath     : str
    TotRmsAbvGrd : str
    YearBuilt    : str
    YearRemodAdd : str
    
@app.post("/response/")
async def response(item: Price):
    model_predict = pickle.load(open('./model.pkl', 'rb'))
        
    list_to_model = [   int(item.OverallQual)
                        ,int(item.GrLivArea)
                        ,int(item.GarageCars)
                        ,int(item.GarageArea)
                        ,int(item.TotalBsmtSF)
                        ,int(item.stFlrSF)
                        ,int(item.FullBath)
                        ,int(item.TotRmsAbvGrd)
                        ,int(item.YearBuilt)
                        ,int(item.YearRemodAdd)
                     ]
    
    print(list_to_model)
    result = model_predict.predict([list_to_model])
    return {"response": f"{result}","data": item}
