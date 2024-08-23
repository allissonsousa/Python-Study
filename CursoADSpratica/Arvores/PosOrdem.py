"""função pos-ordem (registro no *p)
inicio
  se (p->esq != NULO)
      pos-ordem (p->esq);
  se (p->dir != NULO)
      pos-ordem (p->dir);
  visita (p);
fim"""