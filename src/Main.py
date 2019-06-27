from No import No
from ArvoreRubroNegra import ArvoreRubroNegra

print("***************** Arvore Rubro Negra ***********************")

bst = ArvoreRubroNegra()
bst.inserir(50)
bst.inserir(10)
bst.inserir(5)
bst.inserir(60)
bst.inserir(70)
bst.inserir(80)
bst.inserir(81)



print("Pre Ordem")
bst.preorder()
print()
print("em Ordem")
bst.inorder()
print()
print("pos Ordem")
bst.postorder()
print()
print()