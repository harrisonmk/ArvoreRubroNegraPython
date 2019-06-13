from No import No
from ArvoreRubroNegra import ArvoreRubroNegra 
  
print("***************** Arvore Rubro Negra ***********************")   
   
bst = ArvoreRubroNegra()
bst.inserir(8)
bst.inserir(18)
bst.inserir(5)
bst.inserir(15)
bst.inserir(17)
bst.inserir(25)
bst.inserir(40)
bst.inserir(80)
#bst.delete_node(25)
print("Pre Ordem")
bst.preorder()
print()
print("em Ordem")
bst.inorder()
print()
print("pos Ordem")
bst.postorder()
    
