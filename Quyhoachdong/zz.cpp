#include <bits/stdc++.h>
using namespace std;

void z_algorithm(string s, vector<int>& z) {
    int n = s.size(), l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i > r) {
            l = r = i;
            while (r < n && s[r - l] == s[r]) {
                r++;
            }
            z[i] = r - l;
            r--;
        } else {
            int k = i - l;
            if (z[k] < r - i + 1) {
                z[i] = z[k];
            } else {
                l = i;
                while (r < n && s[r - l] == s[r]) {
                    r++;
                }
                z[i] = r - l;
                r--;
            }
        }
    }
}

string replace_all_words(string s, const string& target, const string& replacement) {
    int n = s.size();
    int m = target.size();
    string newStr = target + "$" + s;
    vector<int> z(newStr.size());

    z_algorithm(newStr, z);

    // We'll use a stringstream to build the new string efficiently
    stringstream result;
    int lastPos = 0;

    for (int i = m + 1; i < z.size(); ++i) {
        if (z[i] == m) {
            // Append the part of the string before the match
            result << s.substr(lastPos, i - m - 1 - lastPos);
            // Append the replacement
            result << replacement;
            // Update lastPos to the position after the matched substring
            lastPos = i - m - 1 + m;
        }
    }

    // Append any remaining part of the string
    result << s.substr(lastPos);
    
    return result.str();
}

int main() {
    string s = "So tien phai tra la 1000 dong. Neu khong tra duoc 1000 dong thi se phai tra them lai suat.";
    string p = "1000";
    string replacement = "mot nghin dong";

    cout << "Xau s:\t\t" << s << endl;
    cout << "Xau con p:\t" << p << endl;

    string result = replace_all_words(s, p, replacement);

    cout << "Xau sau khi thay the:\t" << result << endl;

    return 0;
}

