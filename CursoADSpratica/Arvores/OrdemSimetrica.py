"""
função simetrica (registro no *p)
inicio
  se (p->esq != NULO)
      simetrica (p->esq);
  visita (p);
  se (p->dir != NULO)
      simetrica (p->dir);
fim
"""