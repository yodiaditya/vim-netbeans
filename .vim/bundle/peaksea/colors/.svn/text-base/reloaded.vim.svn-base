" Vim colour file: The colorscheme reloaded.
" Maintainer:	Pan, Shi Zhu <go to the URL below for my email>
" URL:		http://vim.sourceforge.net/scripts/script.php?script_id=760
" Last Change:	20 July 2006
" Version:	0.9
"
"	Please prepend [VIM] in the title when writing e-mail to me, or it will
"	be silently discarded.
"
" Description:
"
"	See :h reloaded.txt for details
"
" Release Notes:
"
" v0.9	Added support for new groups such as "guisp" in Vim7.
" v0.8	It was reported that the s:to_hex function has E15 in Vim7, fixed.
" v0.7	Fixed a bug in the first sample
" 	Added the new "channel mixer" grey conversion algorithm, which
" 	improves brightness balance.
" v0.6  For default users it may be slow, Added :se lz to disable refresh
" 	Changed some groups of the sample parameter
" 	Use bracketed variable instead of the exe statement
" 	Changed the order of most division calculation to improve accuracy
" v0.5	Initial upload at 15 July 2004.
"


" minimal value of all the given numbers, maximum 20 parameters
fu! s:min(num1,num2,...)
  let l:min = a:num1<a:num2 ? a:num1 : a:num2

  let l:idx = a:0
  wh l:idx > 0
    let l:var = a:{l:idx}
    if l:var < l:min
      let l:min = l:var
    en
    let l:idx = l:idx - 1
  endw
  retu l:min
endf

" same as above for maximal value
fu! s:max(num1,num2,...)
  let l:max = a:num1>a:num2 ? a:num1 : a:num2

  let l:idx = a:0
  wh l:idx > 0
    let l:var = a:{l:idx}
    if l:var > l:max
      let l:max = l:var
    en
    let l:idx = l:idx - 1
  endw
  retu l:max
endf

" guard the var to be in the range between unity and base.
" if base is omitted, treat like degrees.
fu! s:guard(var,unity,...)
  if a:0
    if a:var < a:1
      retu a:1
    elsei a:var > a:unity
      retu a:unity
    en
    retu a:var
  en
  if a:var < 0
    retu a:unity + (a:var % a:unity)
  en
  retu a:var % a:unity
endf

" sub-function
  " 8-bit integer to 2 digit hexadecimal
  fu! s:to_hex(num)
    retu '0123456789abcdef'[a:num/16%16] . '0123456789abcdef'[a:num%16]
  endf

" rgb to rgb color string
fu! s:rgb2colors(red,green,blue)
  retu "#".s:to_hex(a:red+0).s:to_hex(a:green+0).s:to_hex(a:blue+0)
endf

" sub-functions
  fu! s:hue2rgb(v1, v2, hue)
    " trim to the first period
    let l:hue = s:guard(a:hue, 360)

    if l:hue < 60 
      retu a:v1 + l:hue * (a:v2 - a:v1) / 60
    en
    if l:hue < 180 
      retu a:v2
    en
    if l:hue < 240 
      retu a:v1 + (240 - l:hue) * (a:v2 - a:v1) / 60
    en
    retu a:v1
  endf

" hsl to rgb color string
fu! s:hsb2colors(hue,sat,bri)
  " Hue: Any integer degree (modular 360)
  " Saturation: 0 to 1023/1023
  " Luminance: 0 to 1023/1023
  " RGB results = 0 to 255

  if a:sat == 0
    let l:lum = a:bri / 4
    retu s:rgb2colors(l:lum, l:lum, l:lum)
  en

  if a:bri < 512
    let l:v2 = a:bri * ( 1023 + a:sat )
  el           
    let l:v2 = ( a:bri + a:sat ) * 1023 - ( a:sat * a:bri )
  en

  let l:v1 = 2 * 1023 * a:bri - l:v2

  let l:red = s:hue2rgb(l:v1, l:v2, a:hue + 120) / 4092
  let l:green = s:hue2rgb(l:v1, l:v2, a:hue) / 4092
  let l:blue = s:hue2rgb(l:v1, l:v2, a:hue - 120) / 4092

  retu s:rgb2colors(l:red, l:green, l:blue)

endf

" hsl to v
fu! s:hsb2v(hue,sat,bri)

  if a:sat == 0
    retu a:bri
  en

  if a:bri < 512
    let l:v2 = a:bri * ( 1023 + a:sat )
  el           
    let l:v2 = ( a:bri + a:sat ) * 1023 - ( a:sat * a:bri )
  en

  let l:v1 = 2 * 1023 * a:bri - l:v2

  retu s:hue2rgb(l:v1, l:v2, a:hue + 120) / 1023 * 30 / 100 + 
	\ s:hue2rgb(l:v1, l:v2, a:hue) / 1023 * 58 / 100 + 
	\ s:hue2rgb(l:v1, l:v2, a:hue - 120) / 1023 * 12 / 100

endf


" rgb color number to s:rgb
fu! s:color2rgb(color)
  let s:red = a:color / 0x10000
  let s:green = (a:color / 0x100) % 0x100
  let s:blue = a:color % 0x100
endf

  if !exists("s:loaded") | let s:visual = 0 | en

" rgb to s:hslv
fu! s:rgb2hsb(red,green,blue)

  let l:red = a:red * 1023 / 255
  let l:green = a:green * 1023 / 255
  let l:blue = a:blue * 1023 / 255

  let l:min = s:min(l:red, l:green, l:blue) 
  let l:max = s:max(l:red, l:green, l:blue) 
  let l:delta = l:max - l:min

  let s:bri = (l:max + l:min) / 2

  if l:delta == 0 
    let s:hue = 180	" When sat = 0, hue default to 180
    let s:sat = 0
  el 
    if s:bri < 512 
      let s:sat = l:delta * 1023 / (l:max + l:min)
    el           
      let s:sat = l:delta * 1023 / (2*1023 - l:max - l:min)
    en

    let l:del_r = ( (l:max-l:red) + (l:delta*3) ) * 60 / l:delta
    let l:del_g = ( (l:max-l:green) + (l:delta*3) ) * 60 / l:delta
    let l:del_b = ( (l:max-l:blue) + (l:delta*3) ) * 60 / l:delta

    if l:red == l:max 
      let s:hue = l:del_b - l:del_g
    elsei l:green == l:max  
      let s:hue = 120 + l:del_r - l:del_b
    elsei l:blue == l:max  
      let s:hue = 240 + l:del_g - l:del_r
    en

    let s:hue = s:guard(s:hue, 360)
  en
endf

" sub-functions
  if !exists("s:loaded") | let s:hue_range = 0 | let s:hue_phase = 0 | en
  fu! s:cast_hue(hue)
    retu a:hue * s:hue_range / 360 - s:hue_range / 2 + s:hue_phase 
  endf

  if !exists("s:loaded") | let s:sat_base = 0 | let s:sat_modify = 0 | en
  fu! s:cast_sat(sat)
    let l:sat = a:sat * (1024 - s:sat_base) / 1024 + s:sat_base
    retu l:sat * s:sat_modify / 100
  endf

  if !exists("s:loaded") | let s:bri_base = 0 | let s:bri_modify = 0 | en
  fu! s:cast_bri(bri)
    let l:bri = a:bri * (1024 - s:bri_base) / 1024 + s:bri_base
    retu l:bri * s:bri_modify / 100
  endf

  if !exists("s:loaded") | let s:verbose = 0 | en

" input hsl, do modification in HSL color space, output rgb color string
fu! s:make_hsb(hue,sat,bri)

  let l:hue = s:guard(s:cast_hue(a:hue), 360)
  let l:sat = s:guard(s:cast_sat(a:sat), 1023, s:sat_base)
  let l:bri = s:guard(s:cast_bri(a:bri), 1023, s:bri_base)

  if s:visual
    let l:v1 = s:hsb2v(a:hue, a:sat, l:bri)
    let l:v2 = s:hsb2v(l:hue, l:sat, l:bri)
    if s:verbose | ec "\"\tv1=".l:v1."\tv2=".l:v2."\tL=".l:bri | en

    let l:found = 0
    let l:lastdir = 0
    while v1 != v2
      if v1 < v2 
        if l:found == 0
          let l:bri = l:bri - 10
        el
          let l:bri = l:bri - 1
        en
        if l:lastdir == 1 
          if l:found == 0
            let l:found = 1
          el
            brea
          en
        en
        let l:lastdir = -1

      elsei v1 > v2
        if l:found == 0
          let l:bri = l:bri + 10
        el
          let l:bri = l:bri + 1
        en
        if l:lastdir == -1 
          if l:found == 0
            let l:found = 1
          el
            brea
          en
        en
        let l:lastdir = 1

      en

      if l:bri >= 1023 | brea | en
      if l:bri <= 0 | brea | en

      let l:v2 = s:hsb2v(l:hue, l:sat, l:bri)
      " if (v1 - v2) == 1 | brea | en
      " if (v2 - v1) == 1 | brea | en
    endw

    let l:bri = s:guard(s:cast_bri(l:bri), 1023, s:bri_base)
  en

  if s:verbose | ec "\"\tH=".l:hue."\tS=".l:sat."\tL=".l:bri | en
  retu s:hsb2colors(l:hue, l:sat, l:bri)

endf

" input rgb color number, transfer to HSL, then do <sid>make_hsb
fu! s:make_color(color)
  cal s:color2rgb(a:color)
  cal s:rgb2hsb(s:red, s:green, s:blue)
  retu s:make_hsb(s:hue, s:sat, s:bri)
endf

" input color string, transfer in HSL, output rgb color string
fu! s:parse_color(p)
  if a:p[6] == "#"
    let l:p = '0x'.strpart(a:p, 7, 6) + 0
    retu strpart(a:p, 0, 6).s:make_color(l:p)
  elsei a:p[6] == "@"
    let l:hue = s:guard(strpart(a:p, 7, 3) + 0, 360)
    let l:sat = s:guard(strpart(a:p, 10, 4) + 0, 1023, 0)
    let l:bri = s:guard(strpart(a:p, 14, 4) + 0, 1023, 0)
    retu strpart(a:p, 0, 6).s:make_hsb(l:hue, l:sat, l:bri)
  el
    retu a:p
  en
endf

fu! s:psc_hi(group, p1, p2, ...)
  if a:0 == 0
    let l:p3 = "gui=NONE"
  el
    let l:p3 = a:1
  en
  let l:guisp = 0
  let l:p1 = s:parse_color(a:p1)
  if strpart(l:p1, 0, 6) == "guisp=" | let l:guisp = 1 | en
  let l:p2 = s:parse_color(a:p2)
  if strpart(l:p2, 0, 6) == "guisp=" | let l:guisp = 1 | en
  " for guisp=xxx, if that is undesired, just comment it out
  let l:p3 = s:parse_color(l:p3)
  " guisp is only available for Vim7+
  if strpart(l:p3, 0, 6) == "guisp=" | let l:guisp = 1 | en
  if s:verbose | ec "hi ".a:group." ".l:p1." ".l:p2." ".l:p3 | en
  " version check!
  if l:guisp == 1 && v:version < 700
    retu
  el
    exe "hi ".a:group." ".l:p1." ".l:p2." ".l:p3
  en
endf

fu! s:multi_hi(setting, ...)
  let l:idx = a:0
  wh l:idx > 0
    let l:hlgroup = a:{l:idx}
    if s:verbose | ec "hi ".l:hlgroup." ".a:setting | en
    exe "hi ".l:hlgroup." ".a:setting
    let l:idx = l:idx - 1
  endw
endf

" Transfer global variable into script variable
fu! s:init_option(var, value)
  if !exists("g:psc_".a:var)
    exe "let s:".a:var." = ".a:value
  el
    let s:{a:var} = g:psc_{a:var}
  en
endf

if !exists("loaded") | let s:file = expand("<sfile>") | en

cal s:init_option("reload_prefix", "'".fnamemodify(s:file,":p:h")."/'")

fu! s:psc_reload(...)

  " Only do color for GUI
  if !has("gui_running") | retu | en

  if a:0 > 11
    echoe "Too many parameters, ".'a:0 == '.a:0
    retu
  en

  com! -nargs=+ InitOpt cal s:init_option(<f-args>)

  if a:0 >= 6
    " Hue = phase +- (range/2)
    " Sat = sat * modify% then promoted from base to 1024
    " Bri = bri * modify% then promoted from base to 1024

    let s:hue_range = a:1
    let s:sat_modify = a:2
    let s:bri_modify = a:3

    let s:hue_phase = a:4
    let s:sat_base = a:5
    let s:bri_base = a:6
  el
    InitOpt hue_range 360
    InitOpt sat_modify 100
    InitOpt bri_modify 100

    InitOpt hue_phase 180
    InitOpt sat_base 0
    InitOpt bri_base 0
  en

  if a:0 >= 7
    let s:lightbg = a:7
  el
    InitOpt style 'cool'
    if s:style == 'warm'
      InitOpt lightbg 1
    el
      InitOpt lightbg 0
    en
  en

  if a:0 >= 8 
    let s:plainfont = a:8
  el
    InitOpt fontface 'mixed'
    if s:fontface == 'mixed'
      InitOpt plainfont 0
    el
      InitOpt plainfont 1
    en
  en

  if a:0 >= 9
    let s:visual = a:9
  el
    InitOpt visual 0
  en

  if a:0 >= 10
    let s:verbose = a:10
  el
    InitOpt verbose 0
  en

  if a:0 == 11
    let s:reload_filename = a:11
  el
    InitOpt reload_filename 'ps_color.vim'
  en

  delc InitOpt

  let s:reload_filename = s:reload_prefix.s:reload_filename

  if !filereadable(s:reload_filename)
    echoe "Color data file ".s:reload_filename." not found."
    retu
  en

  se lz

  let s:line = (s:lightbg ? 'se bg=light' : 'se bg=dark' ) . ' | hi clear'
  if s:verbose | ec s:line | en
  exe s:line

  if exists("syntax_on") | sy reset | en

  " This is mandatory, since the "set bg" will have side effect
  let g:colors_name = expand("<sfile>:t:r")


  " GUI:
  "
  " Matrix Reloaded style for gui
  "
  let s:tempfile = '__Temp_Colors__'

  exe "sil! 1new ".s:tempfile
  sil! %d
  exe "sil! 0r ".s:reload_filename
  if s:verbose 
    ec '" Reloaded color scheme from '.s:reload_filename 
    ec '" with param ' s:hue_range s:sat_modify s:bri_modify 
	\ s:hue_phase s:sat_base s:bri_base s:lightbg s:plainfont s:visual
    ec '" '
  en

  if !s:lightbg
    sil! 1,/^\s*" DARK COLOR DEFINE START$/d
    sil! /^\s*" DARK COLOR DEFINE END$/,$d
  el
    sil! 1,/^\s*" LIGHT COLOR DEFINE START$/d
    sil! /^\s*" LIGHT COLOR DEFINE END$/,$d
  en

  sil! 0
  let s:nnb = 1
  com! -nargs=+ PscHi cal s:psc_hi(<f-args>)
  wh 1
    let s:nnb = nextnonblank(s:nnb)
    if !s:nnb | brea | en

    let s:line = getline(s:nnb)

    let s:nnb = s:nnb + 1

    " Skip invalid lines 
    if s:line !~ '^\s*hi\%[ghlight]\s*.*' | con | en

    exe substitute(s:line, '\<hi\%[ghlight]\>', 'PscHi', '')
  endw
  sil! q!
  delc PscHi

  " Enable the bold style
  com! -nargs=+ MultiHi cal s:multi_hi(<f-args>)
  if !s:plainfont
    MultiHi gui=bold Question StatusLine DiffText Statement Type MoreMsg ModeMsg NonText Title VisualNOS DiffDelete TabLineSel
  endif
  delc MultiHi

  " Color Term:
  " Are you crazy?


  " Term:
  " Don't be silly...


  " Links:
  " Something sensible

  exe "sil! 1new ".s:tempfile
  sil! %d
  exe "sil! 0r ".s:reload_filename

  sil! 1,/^\s*" COLOR LINKS DEFINE START$/d
  sil! /^\s*" COLOR LINKS DEFINE END$/,$d

  sil! 0
  let s:nnb = 1
  wh 1
    let s:nnb = nextnonblank(s:nnb)
    if !s:nnb
      brea
    en
    let s:line = getline(s:nnb)

    let s:nnb = s:nnb + 1
    " Skip invalid lines 
    if s:line !~ '^\s*hi\%[ghlight]\s*.*' | con | en

    if s:verbose | ec s:line | en

    sil! exe s:line
  endw
  sil! q!

endf

" To flag the script variables are initialized
let s:loaded = 1

com! -nargs=* Reload cal <SID>psc_reload(<f-args>)

" vim:et:nosta:sw=2:ts=8:
