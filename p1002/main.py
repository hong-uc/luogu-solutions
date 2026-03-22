#include<stdio.h>
int main(){
    int n ,m ,x , y;
    scanf("%d%d%d%d" ,&n,&m,&x,&y);
    long long f[25][25] = {0};
    int dx[] = {0,2,1,-1,-2,-2,-1,1,2};
    int dy[] = {0,-1,-2,-2,-1,1,2,2,1};
    
    int control[25][25] = {0};
    for(int k=0;k <=8;k++)
    {
       int nx = x + dx[k];
       int ny = y + dy[k];
        if(nx>=0&&nx<=n&&ny>=0&&ny<=m){
            control[nx][ny] = 1;
        }
    }
    if(control[0][0] == 0){
        f[0][0] = 1;
    }
    for(int i =0;i<=n;i++){
        for(int j=0;j<=m;j++){
            if(control[i][j]){
                f[i][j] = 0;
                continue;
            }
            if(i==0&&j==0)continue;
            if(i>0){
                f[i][j] +=f[i-1][j];
            }
            if(j>0){
                f[i][j] += f[i][j-1];
            }
            
        }
    }
    printf("%lld",f[n][m]);
    return 0;
}
