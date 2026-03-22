#include<stdio.h>
#define MAXN 10005
int a[MAXN],b[MAXN],g[MAXN],k[MAXN];
int main(){
    int n,x,y;
    scanf("%d",&n);
    for(int i =0;i<=n-1;i++){
        scanf("%d%d%d%d",&a[i],&b[i],&g[i],&k[i]);
    }
    scanf("%d%d",&x,&y);
    int ans = -1;
    for(int i =0;i<n;i++){
        if(x>=a[i]&&x<=a[i]+g[i]&&y>=b[i]&&y<=b[i]+k[i]){
            ans = i+1;
        }
    }
    printf("%d\n",ans);
    return 0;
}
