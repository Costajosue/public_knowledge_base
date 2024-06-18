# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())

N=0
p=0
resultado=0
pontuacoes=[]

while(N<2 or N>10):
	N=int(input())

for i in range(N-1):
	while(p<-100 or p>100):
		p=int(input())
	pontuacoes.append(p)
	
pontuacoes = pontuacoes.sort()

second_index= 0
for i in range(0,N):
	first_index = pontuacoes.index(max(pontuacoes))
	second_index = first =-1
	first = pontuacoes[first_index]
	second = pontuacoes[second_index]
		
	if second < first:
		resultado=second
		break
	