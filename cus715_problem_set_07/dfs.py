
graph = [
#		 A,B,C,D,F
		[0,1,1,0,0],#A
		[1,0,0,1,1],#B
		[1,0,0,0,0],#C
		[0,1,0,0,0],#D
		[0,1,0,0,0]]#F

index_to_vertex = {0:'A',1:'B',2:'C',3:'D',4:'F'}

def dfs(graph, i, visited):
	if not visited[i]:
		print(index_to_vertex[i])
		visited[i] = True
		for j in range(len(graph[i])):
			if graph[i][j]==1:
				dfs(graph,j,visited)

dfs(graph,0,[False]*len(graph))
