# hCaptcha Encryption Analysis
- Since gravilk / bebebebe decided to post the AES-Key's for `6c2596db2ce08d2f8763801d158624c790db3d34b0235bb33999fd85979fac64` (hsw.js), we might as well post some more information shedding some light on HSW's encryption.

## Key Findings

1. **Overestimation of Difficulty**: The complexity of HSW's encryption (AES-GCM) and key location has been exaggerated.

2. **Simplified Key Location**: The process involves pattern-matching to find where i64.store is called 4 times to construct the key. In more obfuscated versions, similar functionality replaces i64.load/store.

3. **Key Extraction Process**:
   - Example of Big Integer conversion:
     ```
     7905493732287749062(n) -> [198, 155, 22, 23, 170, 244, 181, 109]
     3121167419356173726(n) -> [158, 85, 63, 51, 59, 157, 80, 43]
     2242128020943040030(n) -> [30, 110, 66, 69, 142, 163, 29, 31]
     2103398288216998201(n) -> [57, 193, 86, 78, 153, 197, 48, 29]
     ```
   - Conversion method: hex -> decimal -> reverse order
   - Combined result:
     ```
     [57, 193, 86, 78, 153, 197, 48, 29, 30, 110, 66, 69, 142, 163, 29, 31,
      158, 85, 63, 51, 59, 157, 80, 43, 198, 155, 22, 23, 170, 244, 181, 109]
     ```

4. **Key Location Techniques**:
   - For `6c2596db2ce08d2f8763801d158624c790db3d34b0235bb33999fd85979fac64`:
     Search for `i64.store offset=512` and locate preceding i64.store calls.
   - For more obfuscated versions (e.g., `d1285730e6df7d9e9b8c090abc80b36cbbf8722e3655a8d303e084cc7824831a`):
     Search for `end $label3127`.

5. **Extracted Keys**:
   ```python
    self.key_chain = {
       "6c2596db2ce08d2f8763801d158624c790db3d34b0235bb33999fd85979fac64": [57, 193, 86, 78, 153, 197, 48, 29, 30, 110, 66, 69, 142, 163, 29, 31,158, 85, 63, 51, 59, 157, 80, 43,198, 155, 22, 23, 170, 244, 181, 109],
       "d1285730e6df7d9e9b8c090abc80b36cbbf8722e3655a8d303e084cc7824831a": [208, 37, 218, 11, 6, 85, 42, 133, 191, 44, 194, 245, 8, 152, 47, 32, 135, 246, 54, 205, 137, 131, 85, 50, 158, 226, 135, 163, 17, 60, 22, 0]
   }
   ```

## Conclusion
Reversing hCaptcha is less about technical knowledge of WebAssembly and more about persistence and dedication. Success often depends on a combination of luck and time investment.

# Contributors
- @dropout1337: Research and WebAssembly functionality insights
- @notlit69: Key location and time-intensive analysis
