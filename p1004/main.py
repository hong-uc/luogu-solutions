#include<stdio.h>
#include<string.h>
#define MAXN 15 //实际棋盘大小为9*9，15完全够用
int max(int a,int b){
    return a>b?a:b;
}
int main(){
    int grid[MAXN][MAXN];
    int dp[MAXN*2-2][MAXN][MAXN];
    int N;
    scanf("%d",&N);
    int x,y,val;
    memset(grid,0,sizeof(grid));
    while(1)
    {
        scanf("%d%d%d",&x,&y,&val);
        grid[x][y]=val;
        if(x==0&&y==0&&val==0)break;
    }
    memset(dp,0,sizeof(dp));
    dp[0][1][1] = grid[1][1];
    for(int k=1;k<=2*N-2;k++){
        for(int i=1;i<=N&&i<=k+1;i++){
            for(int p=1;p<=N&&p<=k+1;p++){
                int maxVal = 0;
                int j = k+2-i;
                int q = k+2-p;
                if(j<1||j>N||q<1||q>N)continue;
                maxVal=max(maxVal,dp[k-1][i][p]);
                if(i>1)maxVal=max(maxVal,dp[k-1][i-1][p]);
                if(p>1)maxVal=max(maxVal,dp[k-1][i][p-1]);
                if(i>1&&p>1)maxVal=max(maxVal,dp[k-1][i-1][p-1]);

                if(i==p&&j==q){
                    dp[k][i][p] = maxVal + grid[i][j];
                }else{
                    dp[k][i][p] = maxVal + grid[i][j] + grid[p][q];
                }
            }
        }
    }
    printf("%d",dp[2*N-2][N][N]);
    return 0;
}
