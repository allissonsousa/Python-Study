"""função ordem-simetrica-não-recursiva (registro no *p)
inicio
   registro no *aux;
   inteiro momento;
   push (p,1); //insere a raiz de T, no momento 1
   enquanto (pilha não vazia)
      inicio
        pop (aux,momento);
        if (momento == 1)
           inicio
            push (aux,2); //push aux na pilha, momento 2
            se (aux->esq != NULO)
               push (aux->esq,1);
           fim
        if (momento == 2)
           inicio
            visitar (aux);
            se (aux->dir != NULO)
               push (aux->dir,1);
           fim
        // na ordem simétrica, não há ações no momento 3
     fim
fim
"""