#Applicazione in Python ristrutturazione Voli Aerei-Passo 2
#Implementazioni tipi speciali 
from typing import Self
import re

class IntGZ(int):
    # Tipo di dato specializzato Intero > 0

    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, v)

        if value <= 0:
            raise ValueError(f"The value {v} must be greater than zero")
        return value
    
class IntG1900(int):
    # Tipo di dato specializzato Intero > 1900

    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, v)

        if value <= 1900:
            raise ValueError(f"The value {v} must be greater than 1900")
        return value

class IntGEZ(int):
    # Tipo di dato specializzato Intero >= 0

    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, v)

        if value < 0:
            raise ValueError(f"The value {v} must be greater than or equal to zero")
        return value
    
#implementazioni classi Voli Aerei
class Volo:
    def __init__(self, codice: str, durata_minuti: IntGZ):
        self.codice = codice
        self.durata_minuti = durata_minuti
    
    def codice(self) -> str:
        return self.codice

    def durata_minuti(self) -> IntGZ:
        return self.durata_minuti

    def set_codice(self, c: str) -> None:
        self.codice: str = c
    
    def set_durata_minuti(self, dm: IntGZ) -> None:
        self.durata_minuti = dm

class CompagniaAerea:
    def __init__(self, nome: str, anno_fondazione: IntG1900):
        self.nome = nome
        self.anno_fondazione = anno_fondazione
    
    def nome(self) -> str:
        return self.nome

    def anno_fondazione(self) -> IntG1900:
        return self.anno_fondazione

    def set_nome(self, n: str) -> None:
        self.nome: str = n
        
    def set_anno_fondazione(self, af: IntG1900) -> None:
        self.anno_fondazione: IntG1900 = af
    
class Aereoporto:
    def __init__(self, codice: str, nome: str):
        self.codice = codice
        self.nome = nome
    
    def nome(self) -> str:
        return self.nome

    def codice(self) -> str:
        return self.codice

    def set_codice(self, c: str) -> None:
        self.codice: str = c
        
    def set_nome(self, n: str) -> None:
        self.nome: str = n
        
class Città:
    def __init__(self, nome: str, abitanti: IntGEZ):
        self.nome = nome
        self.abitanti = abitanti
        
    def nome(self) -> str:
        return self.nome

    def abitanti(self) -> IntGEZ:
        return self.abitanti

    def set_nome(self, n: str) -> None:
        self.nome: str = n
        
    def set_abitanti(self, a: IntGEZ) -> None:
        self.abitanti: IntGEZ = a
        
class Nazione:
    def __init__(self, nome: str):
        self.nome = nome
        
    def nome(self) -> str:
        return self.nome

    def set_nome(self, n: str) -> None:
        self.nome: str = n