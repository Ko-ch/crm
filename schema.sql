--customersテーブルが既存の場合に削除する
drop table if exists customers;

--customersテーブルを作成する
create table customers(
 name text,
 age integer
);

--初期値を入力する
insert into customers
    (name, age)
values
    ('Bob',15),
    ('Tom',57),
    ('Ken',77)
;