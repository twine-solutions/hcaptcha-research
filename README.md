# hCaptcha Research
- Since gravilk / bebebebe decided to post the AES-Key's for `6c2596db2ce08d2f8763801d158624c790db3d34b0235bb33999fd85979fac64` (hsw.js)
- We might post some more information shedding some light on HSW's encryption.

## Explanation
- For years people have severaly over-hyped the difficulty of HSW's encryption (AES-GCM), specifically locating the keys.
- When all that needed to be done was pattern-match and find the area i64.store was called 4 times to build the key. (In later versions with more obfuscation i64.load/store was removed and replaced with functions that have similar functionality)

- Lets take an example:
  ```
  7905493732287749062(n) -> [198, 155, 22, 23, 170, 244, 181, 109]
  3121167419356173726(n) -> [158, 85, 63, 51, 59, 157, 80, 43]
  2242128020943040030(n) -> [30, 110, 66, 69, 142, 163, 29, 31]
  2103398288216998201(n) -> [57, 193, 86, 78, 153, 197, 48, 29]
  ```
- Each of the Big Integers are being passed to i64.load (this in in `6c2596db2ce08d2f8763801d158624c790db3d34b0235bb33999fd85979fac64`).
- Then the process to convert to the numbers are `hex -> dec -> reverse`
- E.g the result of combining those lists:
  ```
  [57, 193, 86, 78, 153, 197, 48, 29, 30, 110, 66, 69, 142, 163, 29, 31,158, 85, 63, 51, 59, 157, 80, 43,198, 155, 22, 23, 170, 244, 181, 109]
  ```

- To locate those keys in `6c2596db2ce08d2f8763801d158624c790db3d34b0235bb33999fd85979fac64` we'll just search for `i64.store offset=512` and then locate the i64.store's above it. (including the one we searched for)
- And set break points, then grab the value being stored (not the relative address)

- In a more obfuscated version of HSW (`d1285730e6df7d9e9b8c090abc80b36cbbf8722e3655a8d303e084cc7824831a`) we'll search for `end $label3127`. I'll let you do the rest from here.

## Conclusion
- hCaptcha has never been about having the knowledge to reverse engineer it (This covers all fronts of WebAssembly). It's pure luck half the time and the other half is having the time and dedication to put into it.

# Authors
- @dropout1337 - Research & Information on WebAssembly and it's functionality.
- @notlit69 - Spending the time needed to locate the keys.
