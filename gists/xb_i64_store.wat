;; hCaptcha's replacement of i64.store in d1285730e6df7d9e9b8c090abc80b36cbbf8722e3655a8d303e084cc7824831a.

;; Practically just a stored = (var0 ^ var1) & 0xFFFFFFFFFFFFFFFF
;; var0 = value that's being stored (not xor'd)
;; var1 = value that's being passed with i64.xor
;; End result of the i64.xor is being i64.store'd.

(func $xb (;250;) (export "xb") (param $var0 i32) (param $var1 i64) (param $var2 i32)
    (local $var3 i64)
    (local $var4 i64)
    (local $var5 i32)
    (local $var6 i32)
    local.get $var0
    local.get $var2
    i32.add
    local.tee $var2
    i32.const 320
    i32.div_u
    local.set $var5
    local.get $var5
    i32.const 1
    i32.add
    local.tee $var6
    i32.const 3
    i32.shl
    i32.const 120
    i32.add
    local.get $var2
    i32.add
    local.set $var0
    local.get $var5
    call $Eb
    local.get $var6
    call $Eb
    local.get $var2
    i32.const 96
    i32.rem_u
    i64.load offset=4 align=1
    local.get $var1
    i64.xor
    local.set $var1
    local.get $var2
    i32.const 320
    i32.rem_u
    i32.const 312
    i32.sub
    local.tee $var2
    i32.const 0
    i32.gt_s
    if
      i64.const -1
      local.get $var2
      i64.extend_i32_u
      i64.const 3
      i64.shl
      i64.shr_u
      local.tee $var4
      i64.const -1
      i64.xor
      local.set $var3
      local.get $var0
      local.get $var1
      local.get $var4
      i64.and
      local.get $var0
      i64.load align=1
      local.get $var3
      i64.and
      i64.or
      i64.store align=1
      local.get $var0
      local.get $var1
      local.get $var3
      i64.and
      local.get $var0
      i64.load offset=8 align=1
      local.get $var3
      i64.const -1
      i64.xor
      i64.and
      i64.or
      i64.store offset=8 align=1
    else
      local.get $var0
      local.get $var1
      i64.store align=1
    end
  )
