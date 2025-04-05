from pydantic import BaseModel
from typing import Optional, List
from model.passageiro import Passageiro

from schemas import ContatoSchema


class PassageiroSchema(BaseModel):
    """ Define como um novo passageiro a ser inserido deve ser representado
    """
    nome: str = "Joao da Silva"
    cpf: int = 43334543726
    peso: float = 72.50


class PassageiroUpdateSchema(BaseModel):
    """ Define como um passageiro a ser atualizado deve ser representado
    """
    nome: str = "Joao da Silva"
    cpf: int = 43334543726
    peso: float = 72.50

class PassageiroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do passageiro.
    """
    cpf: int = 43334543726


class ListagemPassageirosSchema(BaseModel):
    """ Define como uma listagem de passageiro será retornada.
    """
    passageiros:List[PassageiroSchema]


def apresenta_passageiros(passageiros: List[Passageiro]):
    """ Retorna uma representação do passageiro seguindo o schema definido em
        PassageiroSchema.
    """
    result = []
    for passageiro in passageiros:
        result.append({
            "nome": passageiro.nome,
            "cpf": passageiro.cpf,
            "peso": passageiro.peso,
        })

    return {"passageiros": result}


class PassageiroViewSchema(BaseModel):
    """ Define como um passageiro será retornado: passageiro + contatos.
    """
    id: int = 1
    nome: str = "Joao da Silva"
    cpf: int = 43334543726
    peso: float = 72.50
    total_contatos: int = 1
    contatos:List[ContatoSchema]


class PassageiroDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str



def apresenta_passageiro(passageiro: Passageiro):
    """ Retorna uma representação do passageiro seguindo o schema definido em
        PassageiroViewSchema.
    """
    return {
        "id": passageiro.id,
        "nome": passageiro.nome,
        "cpf": passageiro.cpf,
        "peso": passageiro.peso,
        "total_contatos": len(passageiro.contatos),
        "contatos": [{"texto": c.texto} for c in passageiro.contatos]
    }
