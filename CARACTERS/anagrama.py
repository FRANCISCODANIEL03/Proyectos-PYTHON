"""
FUNCION QUE ANALIZA DOS CADENAS DE TEXTO Y DUEVUELVE SI SON ANAGRMAS O NO
"""

def es_anagrama(c1,c2):
    if len(c1) != len(c2):
        return False
    
    if sorted(c1) == sorted(c2):
        return True
    else:
        return False
    
print(es_anagrama("boca","cabo"))
print(es_anagrama("saul","luis"))
