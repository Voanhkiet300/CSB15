def chan_le(so_nguyen):
    if so_nguyen % 2 == 0:
        return f"{so_nguyen} là chẵn"
    else:
        return f"{so_nguyen}là lẻ"

so_nguyen = int(input("Nhập số nguyên: "))
print(chan_le(so_nguyen))