from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str
    targets: Optional[List[str]] = None
    namespace: Optional[str] = None


class MCPPodsResponse(BaseModel):
    pods: List[Dict[str, Any]]


class MCPConfigMapResponse(BaseModel):
    configmap: Dict[str, Any]
