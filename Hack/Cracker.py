#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <unordered_map>

#define ll long long
#define ld long double
#define pl pair<ll, ll>
#define vi vector<ll>
#define vii vector<vi>
#define vc vector<char>
#define vcc vector<vc>
#define vp vector<pl>
#define mi map<ll,ll>
#define mc map<char,int>
#define sortx(X) sort(X.begin(),X.end());
#define all(X) X.begin(),X.end()
#define ln '\n'
#define YES {cout << "YES\n"; return;}
#define NO {cout << "NO\n"; return;}

const int MODE = 1e9 + 7;

using namespace std;

vi fac(1e6, 1), Bell(1e3, 0);

ll gcdExtended(ll a, ll b, ll* x, ll* y)
{
    if (a == 0) {
        *x = 0, * y = 1;
        return b;
    }
    ll x1, y1;
    ll gcd = gcdExtended(b % a, a, &x1, &y1);
    *x = y1 - (b / a) * x1;
    *y = x1;
    return gcd;
}

ll modeenv(ll n) {
    ll x, y;
    gcdExtended(n, MODE, &x, &y);
    return (x + MODE) % MODE;
}

// nCr = fac(n)/fec(r)*fac(n-r)
ll nCr(ll n, ll r) {
    ll res = fac[n];
    res *= modeenv((fac[r] * fac[n - r]) % MODE);
    return (res) % MODE;
}

//nPr = fac(n) / fac(n - r)
ll nPr(ll n, ll r) {
    ll res = fac[n];
    res *= modeenv(fac[n - r]);
    return (res) % MODE;
}

void INIT() {
    for (int i = 2; i < fac.size(); i++)
        fac[i] = (i * fac[i - 1]) % MODE;


    Bell[0] = Bell[1] = 1;
    for (int i = 2; i < Bell.size(); i++)
        for (int j = 0; j < i; j++)
            Bell[i] = (Bell[i] + nCr(i - 1, j) * Bell[j]) % MODE;
}

void solve(int tc) {


}

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    INIT();
    int size = 1;
    cout << 1;
    //cin >> size;
    for (int i = 1; i <= size; i++)
        solve(i);
}