from typing import Optional, Any
from pydantic import BaseModel

class GraphState(BaseModel):
    query: str
    route: Optional[str]=None
    context: Optional[Any]=None
    answer: Optional[str]=None