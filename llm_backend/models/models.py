import json
from dataclasses import dataclass
from typing import List


@dataclass
class ModelPermission:
    """An LLM model permission"""
    id: str
    object: str
    created: int
    allow_create_engine: bool
    allow_sampling: bool
    allow_logprobs: bool
    allow_search_indices: bool
    allow_view: bool
    allow_fine_tuning: bool
    organization: str
    group: str
    is_blocking: bool

    @classmethod
    def from_json(cls, data):
        """Create a ModelPermission from a JSON object or JSON string."""

        json_data = data
        if isinstance(data, str):
            json_data = json.loads(data)
        return cls(
            id=json_data.get('id'),
            object=json_data.get('object'),
            created=json_data.get('created'),
            allow_create_engine=json_data.get('allow_create_engine'),
            allow_sampling=json_data.get('allow_sampling'),
            allow_logprobs=json_data.get('allow_logprobs'),
            allow_search_indices=json_data.get('allow_search_indices'),
            allow_view=json_data.get('allow_view'),
            allow_fine_tuning=json_data.get('allow_fine_tuning'),
            organization=json_data.get('organization'),
            group=json_data.get('group'),
            is_blocking=json_data.get('is_blocking'),
        )

    def to_json(self):
        """Convert the ModelPermission to a JSON object."""
        return {
            "id": self.id,
            "object": self.object,
            "created": self.created,
            "allow_create_engine": self.allow_create_engine,
            "allow_sampling": self.allow_sampling,
            "allow_logprobs": self.allow_logprobs,
            "allow_search_indices": self.allow_search_indices,
            "allow_view": self.allow_view,
            "allow_fine_tuning": self.allow_fine_tuning,
            "organization": self.organization,
            "group": self.group,
            "is_blocking": self.is_blocking,
        }


@dataclass
class Model:
    """An LLM model. It has a name and one or more permissions."""
    id: str
    object: str
    created: int
    owned_by: str
    permission: List[ModelPermission]
    root: str
    parent: str

    @classmethod
    def from_json(cls, data):
        """Create a Model from a JSON object or JSON string."""

        json_data = data
        if isinstance(data, str):
            json_data = json.loads(data)
        return cls(
            id=json_data.get('id'),
            object=json_data.get('object'),
            created=json_data.get('created'),
            owned_by=json_data.get('owned_by'),
            permission=[ModelPermission.from_json(perm) for perm in json_data.get('permission')],
            root=json_data.get('root'),
            parent=json_data.get('parent'),
        )

    def to_json(self):
        """Convert the model to a JSON object."""
        return {
            "id": self.id,
            "object": self.object,
            "created": self.created,
            "owned_by": self.owned_by,
            "permission": [perm.to_json() for perm in self.permission],
            "root": self.root,
            "parent": self.parent,
        }


@dataclass
class ModelResponse:
    """Dataclass for a model response"""
    object: str
    data: List[Model]

    @classmethod
    def from_json(cls, data):
        """Create a ModelResponse from a JSON object."""

        json_data = data
        if isinstance(data, str):
            json_data = json.loads(data)
        return cls(
            object=json_data.get('object'),
            data=[Model.from_json(mdl) for mdl in json_data.get('data')],
        )

    def to_json(self):
        """Convert the response to a JSON object."""
        return {
            "object": self.object,
            "data": [model.to_json() for model in self.data],
        }
