from typing import List

from pydantic import BaseModel, Field


class GraphConfig(BaseModel):
    allowed_nodes: List[str] = Field(
        ..., description="List of allowed nodes in the graph"
    )
    allowed_relationships: List[str] = Field(
        ..., description="List of allowed relationships in the graph"
    )
