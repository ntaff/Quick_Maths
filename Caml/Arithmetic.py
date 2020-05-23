let rec egcd a b =
   if b = 0 then (1, 0)
   else
      let q = a/b and r = a mod b in
      let (s, t) = egcd b r in
         (t, s - q*t)


let mod_inv a b =
   let (x, y) = egcd a b in
      if a*x + b*y = 1 then Some x else None
