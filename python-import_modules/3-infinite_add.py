#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    # sys.argv[1:] ilə skriptin adını kənarlaşdırıb yalnız rəqəmləri götürürük
    for arg in sys.argv[1:]:
        total += int(arg)
    print("{}".format(total))
