#!/usr/bin/env python3
import imported
import sub

if __name__ == "__main__":
    print(id(imported.a))
    print(sub.show_id())
    print(id(sub.imported.a))

