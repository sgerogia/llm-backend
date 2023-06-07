from llm_backend.controllers import models


def test_listModels(set_openai_key, set_logger):
    # act
    res = models.listModels()
    # assert
    assert res[1] == 200
    assert len(res[0].data) > 0
    assert res[0].object == 'list'


def test_retrieveModel(set_openai_key, set_logger):
    # act
    res = models.retrieveModel('ada')
    # assert
    assert res[1] == 200
    assert res[0].id == 'ada'