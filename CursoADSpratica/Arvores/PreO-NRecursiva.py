"""função pre-ordem-não-recursiva (registro no *p)
inicio
   registro no *aux;
   inteiro momento;
   push (p,1); //insere a raiz de T, no momento 1
   enquanto (pilha não vazia)
      inicio
        pop (aux,momento);
        if (momento == 1)
           inicio
            visitar (aux);//caso se deseje a pré-ordem
            push (aux,2); //push aux na pilha, momento 2
            se (aux->esq != NULO)
               push (aux->esq,1);
           fim
        if (momento == 2)
           inicio
            push (aux,3); //push aux na pilha, momento 3
            se (aux->dir != NULO)
               push (aux->dir,1);
           fim
        // na pré-ordem, não há ações no momento 3
     fim
fim"""