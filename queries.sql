
create table Kisiler(
  id integer primary key autoincrement,
  nickname text,
  yas int,
  cinsiyet varchar(1),
  ulke text,
  dil text,
  meslek tex,
  tercihler text
  );

insert into Kisiler (nickname, yas, cinsiyet, ulke, dil, meslek, tercihler) values(
"Ali",29,"E","TR","Turkce","Muhendis","Aksiyon,Komedi");
insert into Kisiler (nickname, yas, cinsiyet, ulke, dil, meslek, tercihler) values(
"Veli",29,"E","EN","Turkce","ogrenci","Aksiyon,Komedi");
insert into Kisiler (nickname, yas, cinsiyet, ulke, dil, meslek, tercihler) values(
"Derya",29,"K","TR","Turkce","Muhendis","Aksiyon,Komedi");

select * from Kisiler;
select nickname from Kisiler;

update Kisiler set nickname="Faruk" where id = 2; 
select * from Kisiler;

select * from Kisiler order by yas;


select avg(yas) from Kisiler;

select meslek,count(meslek) from Kisiler group by meslek; 

alter table Kisiler add column email text;
update Kisiler set email = "ali at gmail.com" where id = 2;
select * from Kisiler;

create table Filmler(
id integer primary key autoincrement,
film_ismi text not null,  /*not null: bış bıakılamayan satırlar*/
film_turu text not null,
puani float,
yonetmen text,
oyuncular text
); 

insert into Filmler(film_ismi,film_turu,puani,yonetmen,oyuncular) values(
"Interstellar", "Sci-fi", 8.7, "Christopher Nolan", "Anne Hathaway");

insert into Filmler(film_ismi,film_turu,puani,yonetmen,oyuncular) values(
"Sekerpare", "Komedi", 8.7, "Atif Yilmaz", "Ilyas Salman");

insert into Filmler(film_ismi,film_turu,puani,yonetmen,oyuncular) values(
"Copcular Krali", "Komedi", 8.7, "Zeki Okten", "Kemal Sunal");

select * from Filmler;

select * from Kisiler inner join Filmler on Filmler.id = Kisiler.id; 
/*Kişiler tablosundaki id sütununu Filmler tablosundaki id ile eşitleyip, 
Kişiler tablosunun sonuna Filmler tablsonu ekler*/

create temporary table isimler_tablo(id integer primary key, isim text);
select * from isimler_tablo;

insert into isimler_tablo(isim) values ("Huseyin");

insert into isimler_tablo(isim) select nickname from Kisiler; 
/*Kişiler tablosundaki nickname sütununu alır, isimler_tablos tablosundaki isimler sütununa ekler*/
select * from isimler_tablo;

create table silinen_bilgiler(id integer primary key autoincrement, isim text);

create trigger t1 after delete on isimler_tablo 
begin
  insert into silinen_bilgiler(isim) values(old.isim);
end;

delete from isimler_tablo where id=3;
select * from silinen_bilgiler;


