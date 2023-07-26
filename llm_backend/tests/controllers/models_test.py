from llm_backend.constants import MODEL_LLAMA, MODEL_OPENAI
from llm_backend.controllers.models import init


def test_init_modelscontroller(llama_params, openai_params, set_logger):
    # arrange
    params = {**llama_params, **openai_params}

    # act
    cont = init(params=params, log=set_logger)

    # assert
    assert len(cont) == 2
    assert cont[MODEL_LLAMA] is not None
    assert cont[MODEL_OPENAI] is not None


def test_listModels_openai(openai_client, set_logger):
    # act
    res = openai_client.get('/v1/models')

    # assert
    assert res.status_code == 200
    assert res.json['object'] == 'list'
    models = res.json['data']
    assert len(models) > 0
    found: bool = False
    for model in models:
        if model['owned_by'] == 'openai':
            found = True
            break
    assert found is True


def test_listModels_llama(llama_client, set_logger):
    # act
    res = llama_client.get('/v1/models')

    # assert
    assert res.status_code == 200
    assert res.json['object'] == 'list'
    models = res.json['data']
    length = len(models)
    assert length > 0
    found: bool = False
    for model in models:
        if model['id'] == MODEL_LLAMA:
            found = True
            break
    assert found is True


def test_retrieveModel_openai(openai_client, set_logger):
    # act
    res = openai_client.get('/v1/models/babbage')

    # assert
    assert res.status_code == 200
    assert res.json['object'] == 'model'
    assert res.json['id'] == 'babbage'


def test_retrieveModel_llama(llama_client, set_logger):
    # act
    res = llama_client.get('/v1/models/llama')

    # assert
    assert res.status_code == 200
    assert res.json['object'] == 'model'
    assert res.json['id'] == 'llama'
