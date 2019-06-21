program fibonacci;
uses crt;
var
 a,b,c,max:integer;
begin //empieza
clrscr;
 writeln('Serie de Fibonacci');
 writeln('Teclea el numero tope de la serie');
 writeln('');
 readln(max);
 a:=1;
 b:=1;
 wrtite('texto') //cadena
 writeln(a);
 writeln(b);
 while (a+b)<=max do
  begin;
  c:=(a+b);
  writeln(c);
  a:=b;
  b:=c;
  end;
 readln;
 (*
 multilinea
 *)
end.
