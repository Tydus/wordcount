#include <cstdio>
#include <iostream>
#include <string>

struct Node {
  static constexpr int kRadix = 26;
  size_t count;
  Node *next[kRadix];
};

Node *insert() {
  Node *root = new Node;

  int c;
  Node *n = root;
  while ((c = fgetc(stdin)) > 0) {
    if (c == '\n') {
      ++n->count;
      n = root;
      continue;
    }

    // convert ASCII to index, letters only
    c -= (c >= 'a' && c <= 'z') ? 'a' : 'A';
    if (!n->next[c]) n->next[c] = new Node();
    n = n->next[c];
  }
  return root;
}

void dump(const Node *n, std::string &prefix) {
  if (n->count) printf("%zu: %s\n", n->count, prefix.c_str());
  for (int i = 0; i < Node::kRadix; ++i) {
    if (!n->next[i]) continue;
    prefix.push_back('a' + i);
    dump(n->next[i], prefix);
    prefix.pop_back();
  }
}

void stats() {
  size_t count[256] = {0};
  int c;
  while ((c = fgetc(stdin)) > 0) ++count[c + 128];
  for (int i = 0; i < 256; ++i) printf("%c %d %zu\n", i - 128, i - 128, count[i]);
}

int main(int argc, char *argv[]) {
  freopen("../enwik8-ascii.txt", "rb", stdin);
  std::string base;
  dump(insert(), base);
  return 0;
}
