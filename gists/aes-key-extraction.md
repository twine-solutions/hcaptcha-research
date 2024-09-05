# AES Key Extraction

## Step 1: Identify Relevant Instructions
In the WAT code, look for `i64.store` instructions with `offset` values from 8 to 32. These store the key in memory. The relevant lines look like this:

```wat
i64.const -5326938611351612412
i64.store offset=32 align=1

i64.const 8813716308508918095
i64.store offset=24 align=1

i64.const -7086638283704341346
i64.store offset=16 align=1

i64.const 5826795411065202142
i64.store offset=8 align=1
```

## Step 2: Convert Constants to Hexadecimal
- [-5326938611351612412](https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=-5326938611351612412) -> B612E98E6A131404
- [8813716308508918095](https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=8813716308508918095)   -> 7A509C4917BDC14F
- [-7086638283704341346](https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=-7086638283704341346) -> 9DA73407101E6C9E
- [5826795411065202142](https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=5826795411065202142)   -> 50DCEF8DFF6AE5DE

## Step 3: Convert Hexadecimal to Decimal
[hex-dec.js](hex-dec.js)
- B6 12 E9 8E 6A 13 14 04 -> 182 18 233 142 106 19 20 4
- 7A 50 9C 49 17 BD C1 4F -> 122 80 156 73 23 189 193 79
- 9D A7 34 07 10 1E 6C 9E -> 157 167 52 7 16 30 108 158
- 50 DC EF 8D FF 6A E5 DE -> 80 220 239 141 255 106 229 222

## Step 4: Reverse the order
- Offset 8:  80 220 239 141 255 106 229 222
- Offset 16: 157 167 52 7 16 30 108 158
- Offset 24: 122 80 156 73 23 189 193 79
- Offset 32: 182 18 233 142 106 19 20 4

## Step 5: Reverse the order of the numbers
- 80 220 239 141 255 106 229 222 -> 222 229 106 255 141 239 220 80
- 157 167 52 7 16 30 108 158     -> 158 108 30 16 7 52 167 157
- 122 80 156 73 23 189 193 79    -> 79 193 189 23 73 156 80 122
- 182 18 233 142 106 19 20 4     -> 4 20 19 106 142 233 18 182

## Step 6: Hey presto!
- Our result:
```js
[
    222, 229, 106, 255, 141, 239, 220, 80,
    158, 108, 30, 16, 7, 52, 167, 157, 79,
    193, 189, 23, 73, 156, 80, 122, 4, 20,
    19, 106, 142, 233, 18, 182,
]
```
- Code inside Rust:
```rust
let key_bytes: [u8; 32] = [
    222, 229, 106, 255, 141, 239, 220, 80,
    158, 108, 30, 16, 7, 52, 167, 157, 79,
    193, 189, 23, 73, 156, 80, 122, 4, 20,
    19, 106, 142, 233, 18, 182,
];
```

# Author
- @dropout1337
