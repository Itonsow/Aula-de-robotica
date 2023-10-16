'''
git add .
atualiza com os arquivos do git
'''

'''
git commit -n "msg"
git push origin master
'''
import numpy as np
import RobPy as rp


'''
M = rp.matriz_rotacao_x(43*np.pi/180)
r = rp.cria_vetor3([2, 3, 1])
v_b = np.asarray([1, 1, 0])
v_a = rp.constroi_vetor(v_b, m_rot_b_a=M, v_o_a=r)
print(v_a)
'''
M = rp.matriz_rotacao_x(43*np.pi/180)
r = rp.cria_vetor3([2, 3, 1])

T = rp.cria_operador4(M, r)
print(T)