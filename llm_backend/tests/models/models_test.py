from llm_backend.models.models import ModelResponse


def test_parse_modelresponse():
    # arrange
    data = """{
    "object": "list",
    "data": [
                {
                    "id": "babbage",
                    "object": "model",
                    "created": 1649358449,
                    "owned_by": "openai",
                    "permission": [
                        {
                            "id": "modelperm-49FUp5v084tBB49tC4z8LPH5",
                            "object": "model_permission",
                            "created": 1669085501,
                            "allow_create_engine": false,
                            "allow_sampling": true,
                            "allow_logprobs": true,
                            "allow_search_indices": false,
                            "allow_view": true,
                            "allow_fine_tuning": false,
                            "organization": "*",
                            "group": null,
                            "is_blocking": false
                        }
                    ],
                    "root": "babbage",
                    "parent": null
                }
            ]
    }"""

    # act
    res = ModelResponse.from_json(data)

    # assert
    assert res.object == 'list'
    assert len(res.data) == 1
    assert res.data[0].id == 'babbage'
    assert res.data[0].object == 'model'
    assert res.data[0].created == 1649358449
    assert res.data[0].owned_by == 'openai'
    assert len(res.data[0].permission) == 1
    assert res.data[0].permission[0].id == 'modelperm-49FUp5v084tBB49tC4z8LPH5'
    assert res.data[0].permission[0].object == 'model_permission'
    assert res.data[0].permission[0].created == 1669085501
    assert res.data[0].permission[0].allow_create_engine is False
    assert res.data[0].permission[0].allow_sampling is True
    assert res.data[0].permission[0].allow_logprobs is True
    assert res.data[0].permission[0].allow_search_indices is False
    assert res.data[0].permission[0].allow_view is True
    assert res.data[0].permission[0].allow_fine_tuning is False
    assert res.data[0].permission[0].organization == '*'
    assert res.data[0].permission[0].group is None
    assert res.data[0].permission[0].is_blocking is False
