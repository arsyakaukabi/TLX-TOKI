n,f,d=map(int,input().split());print('NYOE S'[f<=n and f*(f+1)//2<=d<=sum([min(i,f+n-i) for i in range(1,n+1)])::2])